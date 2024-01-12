from flask import Blueprint as bp, render_template,request
from flask_socketio import SocketIO, emit
import logging

module13_bp = bp('module13', __name__)
socketio13 = SocketIO()


logger = logging.getLogger(__name__)

@module13_bp.route('/task13',methods=['POST'])
def task13():
    return render_template("advance/module13_result.html")

@socketio13.on('notification')
def handle_notification(data):
    message = data['message']
    emit('new_notification', {'message': message}, broadcast=True)



def Create_app():
    return socketio13