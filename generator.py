import time
from typing import Generator

# --- 1. Sample Large Dataset Simulation ---
# In a real-world scenario, this list might contain millions of items
# read directly from a file or database cursor.
#

MOCK_USER_DATA: list[dict[str, any]] = [
    {"id": 1, "username": "alice_smith", "status": "active", "age": 28},
    {"id": 2, "username": "bob_jones", "status": "inactive", "age": 45},
    {"id": 3, "username": "charlie_brown", "status": "active", "age": 33},
    {"id": 4, "username": "diana_prince", "status": "active", "age": 22},
    {"id": 5, "username": "evan_peters", "status": "pending", "age": 51},
    # Imagine thousands more entries here...
]

# --- 2. The Generator Function ---
def process_user_data(data: list[dict[str, any]]) -> Generator[dict[str, any], None, None]:
    """
    Processes user records one by one, yielding the result immediately.

    This function uses 'yield' instead of 'return' to make it a generator.
    It does not build a large list of processed results in memory.
    """
    print("--- Generator Initialized ---")

    for user in data:
        # Simulate a complex, time-consuming operation (like fetching external data or heavy computation)
        # For a truly massive list, this ensures the program doesn't stall for too long at any point.
        time.sleep(1)

        # Perform the processing
        processed_user = {
            "user_id": user['id'],
            # Example transformation: Uppercasing the username
            "display_name": user['username'].upper(),
            "is_senior": user['age'] >= 50,
            "original_status": user['status']
        }

        # The 'yield' keyword returns the value and pauses the function's state.
        # When the next item is requested, execution resumes right after the yield.
        yield processed_user

    print("--- Generator Finished Processing All Data ---")
