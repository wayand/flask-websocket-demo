# Flask WebSocket Demo

A simple Flask application demonstrating real-time communication using WebSockets with the `flask-sock` library.

## Features

- **Real-time WebSocket communication** between client and server
- **Interactive web interface** for sending messages
- **Dynamic data processing** with live feedback
- **Error handling** for invalid inputs
- **Live timestamp display** for each processed row

## Demo Functionality

The application provides a simple row processing demonstration where:
- Users enter a range value through a web form
- The server processes numbers from 0 to the specified range
- Each row is sent back to the client in real-time with a timestamp
- Progress and completion status are displayed live in the browser

## Installation

1. Clone or download this repository
2. Install the required dependencies:
   ```bash
   pip install flask flask-sock
   ```

## Usage

1. Run the Flask application:
   ```bash
   python main.py
   ```

2. Open your web browser and navigate to:
   ```
   http://localhost:5000
   ```

3. Enter a number in the input field and press Enter to start the processing
4. Watch as the server processes each row and sends real-time updates

## Project Structure

```
flask-websocket/
├── main.py              # Flask application with WebSocket routes
├── templates/
│   └── index.html       # Web interface with WebSocket client
└── README.md           # This file
```

## How It Works

### Server Side (`main.py`)
- **Flask Route (`/`)**: Serves the main HTML page
- **WebSocket Route (`/logs`)**: Handles WebSocket connections and message processing
- **Script Function**: Processes the range input and sends incremental updates

### Client Side (`templates/index.html`)
- **WebSocket Connection**: Connects to the `/logs` WebSocket endpoint
- **Form Handling**: Captures user input and sends it via WebSocket
- **Live Updates**: Displays incoming messages from the server in real-time

## WebSocket Communication Flow

1. Client connects to WebSocket endpoint (`ws://localhost:5000/logs`)
2. User enters a range value in the web form
3. Client sends the range value to the server via WebSocket
4. Server validates the input and processes the range
5. Server sends each row update back to the client in real-time
6. Client displays the updates in the browser

## Error Handling

The application includes error handling for:
- **Invalid input**: Non-integer values
- **Invalid range**: Values less than 1
- **Connection issues**: WebSocket disconnections and errors

## Dependencies

- **Flask**: Web framework for Python
- **flask-sock**: WebSocket support for Flask applications

## Configuration

The application uses a secret key for Flask-Sock configuration. In production, make sure to use a secure secret key and set it via environment variables.

## Development

To extend this demo:
- Modify the `script()` function to process different types of data
- Add authentication for WebSocket connections
- Implement multiple WebSocket channels for different functionalities
- Add database integration for persistent data processing

## License

This is a demo project for educational purposes.
