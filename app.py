import os
from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

# Importing database functions provided by the team (Member 2)
from init_db import init_db, save_message, get_all_messages

app = Flask(__name__)
app.config['SECRET_KEY'] = 'first_contact_secure_key_2026'

# Initialize SocketIO with cross-origin access enabled for local network devices
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize SQLite database and tables on application startup
init_db()


# 1. Main Route: Serves the primary web dashboard to connected clients
@app.route('/')
def index():
    return render_template('index.html')


# 2. Connection Event: Standard log when a device joins the local network
@socketio.on('connect')
def handle_connect():
    print(f"[CONNECTED] Device connected: {request.sid}")


# 3. Dedicated History Event: Fetches and sends chat history upon explicit frontend request
@socketio.on("request_chat_history")
def send_chat_history():
    print(f"[HISTORY REQUEST] Fetching database logs for client: {request.sid}")
    
    # Retrieve raw tuples from SQLite DB
    history = get_all_messages()
    
    # Format database tuples into a clean JSON list for the frontend
    formatted_history = []
    for msg in history:
        formatted_history.append({
            "sender": msg[0],            # sender_name
            "text": msg[1],              # message_text
            "timestamp": msg[2],         # timestamp
            "is_broadcast": bool(msg[3]) # is_broadcast converted to boolean
        })
    
    # Emit only to the specific client who made the request (unicast)
    emit("chat_history", formatted_history, to=request.sid)


# 4. WebSocket Event: Handles standard peer-to-peer chat room messaging
@socketio.on('send_message')
def handle_message(data):
    """
    Triggered when a user sends a normal text message.
    Expected data format: {'sender': 'John', 'text': 'Help required'}
    """
    sender = data.get('sender', 'Anonymous').strip()
    message_text = data.get('text', '')

    # Validation: Reject empty or whitespace-only messages
    if not message_text.strip():
        return False

    print(f"[CHAT] {sender}: {message_text.strip()}")

    # Save normal message to database via the integrated module
    save_message(
        sender_name=sender,
        message_text=message_text.strip(),
        is_broadcast=False
    )

    # Broadcast the message in real-time to everyone on the network
    emit('receive_message', {
        'sender': sender,
        'text': message_text.strip(),
        'is_broadcast': False
    }, broadcast=True)


# 5. WebSocket Event: Handles high-priority emergency alerts
@socketio.on('broadcast_alert')
def handle_alert(data):
    """
    High-priority broadcast flashed across the top banner of all active screens.
    Expected data format: {'sender': 'Admin', 'text': 'Evacuate immediately'}
    """
    sender = data.get('sender', 'Emergency Coordinator').strip()
    alert_text = data.get('text', '')

    # Validation: Reject empty or whitespace-only alerts
    if not alert_text.strip():
        return False

    print(f"[ALERT] {sender}: {alert_text.strip()}")

    # Save critical alert to database with is_broadcast set to True
    save_message(
        sender_name=sender,
        message_text=alert_text.strip(),
        is_broadcast=True
    )

    # Instantly push the critical alert to all clients on the local network
    emit('receive_message', {
        'sender': sender,
        'text': alert_text.strip(),
        'is_broadcast': True
    }, broadcast=True)


if __name__ == '__main__':
    # Binds the server to 0.0.0.0 to enable local Wi-Fi Hotspot sharing on port 5000
    socketio.run(
        app,
        host='0.0.0.0',
        port=5000,
        debug=True
    )