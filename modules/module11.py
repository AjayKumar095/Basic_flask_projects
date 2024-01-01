from flask import Blueprint as bp, render_template
from flask_socketio import SocketIO,send
import logging

module11_bp = bp('module11', __name__)
socketio = SocketIO()
logger = logging.getLogger(__name__)

@module11_bp.route('/task11', methods=["POST"])
def task11():
    return render_template("module11_result.html")

@socketio.on('message')
def handle_message(message):
    logger.info(f"Checking for the received message: {message}")
    print("Recived message"+message)
    socketio.send(message, broadcast=True)
    