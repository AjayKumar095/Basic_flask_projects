from flask import Blueprint as bp, render_template,request
from flask_socketio import SocketIO, emit
import logging

module13_bp = bp('module13', __name__)
socketio = SocketIO()


logger = logging.getLogger(__name__)

@module13_bp.route('/task13',methods=['POST'])
def task13():
    return render_template("advance/module13_result.html")

@socketio.on('message')
def handle_message(message):
    logger.info(f"Checking for the received message: {message}")
    emit('message', {'senderId': request.sid, 'text': message}, broadcast=True)


def Create_app():
    return socketio  
