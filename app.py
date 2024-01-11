# Importing basic modules
from flask import Flask, render_template
from flask_socketio import SocketIO
from flask_login import LoginManager
import logging

# Importing app modules.
from modules.module1 import module1_bp
from modules.module2 import module2_bp
from modules.module3 import module3_bp
from modules.module4 import module4_bp
from modules.module5 import module5_bp
from modules.module6 import module6_bp
from modules.module7 import module7_bp
#from modules.module8 import module8_bp,users
from modules.module10 import module10_bp
from modules.module9 import module9_bp
from modules.module11 import module11_bp, socketio
from modules.module12 import module12_bp, socketio

# Declaring flask app.
app = Flask(__name__)
logging.basicConfig(filename='static/app.log', level=logging.INFO) # logging 


app.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # Declaring a maximum file size to upload.
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['TEMPLATES_AUTO_RELOAD'] = True



# Registering the modules with app.
app.register_blueprint(module1_bp, url_prefix='/module1')
app.register_blueprint(module2_bp, url_prefix='/module2')
app.register_blueprint(module3_bp, url_prefix='/module3')
app.register_blueprint(module4_bp, url_prefix='/module4')
app.register_blueprint(module5_bp, url_prefix='/module5')
app.register_blueprint(module6_bp, url_prefix='/module6')
app.register_blueprint(module7_bp, url_prefix='/module7')
#app.register_blueprint(module8_bp, url_prefix='/module8')
app.register_blueprint(module9_bp, url_prefix='/module9')
app.register_blueprint(module10_bp, url_prefix='/module10')
app.register_blueprint(module11_bp, url_prefix='/module11')
app.register_blueprint(module12_bp, url_prefix='/module12')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    socketio.init_app(app)
    socketio.run(app, debug=True, port=5000)
    

