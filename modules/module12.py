from flask import Blueprint as bp, render_template,request
from flask_socketio import SocketIO, emit
import logging

module12_bp = bp('module12', __name__)
socketio = SocketIO()


logger = logging.getLogger(__name__)

@module12_bp.route('/task12',methods=['POST'])
def task12():
    return render_template("advance/module12_result.html")

@socketio.on('message')
def handle_message(message):
    logger.info(f"Checking for the received message: {message}")
    print('Received message:', message)
    emit('message', {'senderId': request.sid, 'text': message}, broadcast=True)
    
def create_app():
    return socketio  

