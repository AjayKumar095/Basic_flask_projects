from flask import Blueprint as bp, render_template,request
from flask_socketio import SocketIO, emit
import logging

module11_bp = bp('module11', __name__)
socketio = SocketIO()


logger = logging.getLogger(__name__)

@module11_bp.route('/task11',methods=['POST'])
def task11():
    return render_template("advance/module11_result.html")

@socketio.on('message')
def handle_message(message):
    logger.info(f"Checking for the received message: {message}")
    print('Received message:', message)
    emit('message', {'senderId': request.sid, 'text': message}, broadcast=True)
    
def Create_app():
    return socketio  

