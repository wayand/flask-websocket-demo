from flask import Flask, render_template
from flask_sock import Sock

import time

app = Flask(__name__)

app.config['SECRET_KEY'] = 'a_secure_secret_key_for_flask_sock'
sock = Sock(app)

@app.route("/")
def index():
    return render_template("index.html")

@sock.route("/logs")
def logs(ws):
    """
    Websocket endpoint. Receives the range value and executes the script.
    """
    while True: # <--- Added while loop to keep the connection alive
        try:
            range_input = ws.receive()
            if range_input is None: # Client disconnected gracefully
                break
            if range_input:
                script(ws, range_input)
            else:
                ws.send("No input received. Please enter a range value.")
        except Exception as e:
            print(f"Websocket connection closed or error: {e}")
            break

def script(ws, range_input):
    """
    Executes a loop up to the given range and sends the output
    back to the client via the provided websocket connection.
    """
    try:
        # Convert the input string to an integer
        range_value = int(range_input)
    except ValueError:
        ws.send("Error: The input must be a valid integer.")
        return

    if range_value < 1:
        ws.send("Error: Range must be 1 or greater.")
        return

    ws.send(f"Script started! Processing up to {range_value} rows...")

    for i in range(range_value):
        message = f"Row no.: {i} (Timestamp: {time.strftime('%H:%M:%S')})"
        ws.send(message)
        time.sleep(0.05) # Small delay to simulate processing time

    ws.send("--- Script Finished ---")
    ws.send(f"Total rows processed: {range_value}")
