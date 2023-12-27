from flask import Flask, render_template

from modules.module1 import module1_bp
from modules.module2 import module2_bp
from modules.module3 import module3_bp
from modules.module4 import module4_bp
from modules.module5 import module5_bp
from modules.module6 import module6_bp

app = Flask(__name__)
app.secret_key = 'fjjkf857fdjft548jnvfKJJNjhdfd'

app.register_blueprint(module1_bp, url_prefix='/module1')
app.register_blueprint(module2_bp, url_prefix='/module2')
app.register_blueprint(module3_bp, url_prefix='/module3')
app.register_blueprint(module4_bp, url_prefix='/module4')
app.register_blueprint(module5_bp, url_prefix='/module5')
app.register_blueprint(module6_bp, url_prefix='/module6')

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')

