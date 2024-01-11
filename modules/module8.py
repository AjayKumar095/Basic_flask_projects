from flask import Blueprint as bp, render_template , request, redirect, url_for

from flask_bcrypt import Bcrypt
import json
import logging
module8_bp=bp("module8", __name__)
logger = logging.getLogger(__name__)
#JSON_FILE = 'static/users.json'

try:
    with open('static/users.json', 'r') as file:
        users = json.load(file)
except FileNotFoundError:
    users = []

def save_users():
    with open('static/users.json', 'w') as file:
        json.dump(users, file, indent=2)


       
@module8_bp.route("/task8", methods=["POST","GET"])
def task8():
    try: 
       return render_template("intermediate/module8_result.html")
    except Exception:
        return  """<h1 style="color: red; text-align: center;">404 Page Not Found</h1>
            <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""


@module8_bp.route("/login", methods=["POST","GET"])
def login():
    if request.method=="POST":
        if "login" in request.form:
            logger.info("enter in login form")
            get_username=request.form.get("loginUsername")
            get_password=request.form.get("loginPassword")
            with open('static/users.json', 'r') as file:
                logger.info("open user file")
                Users=json.load(file)
            for user in Users:
                logger.info("enter in for loop")
                if  user["username"] == get_username and get_password==user["password"]:
                    logger.info("enter in if block")
                    return redirect(url_for("module8.dashboard", username=get_username))
            #return "error"

@module8_bp.route("/signup", methods=["POST","GET"])
def signup():
    
    if request.method=="POST":
        if "sign_up" in request.form:
            username=request.form.get('signupUsername')
            password=request.form.get("signupPassword")
            users.append({'username': username, 'password': password})
            save_users()
            return  redirect(url_for("module8.dashboard", username=username))
        else:
            return "error"    

@module8_bp.route("/dashboard/<username>")
def dashboard(username):
    logger.info("enter in function")
    try:
        logger.info("enter in try block dash")
        return render_template("intermediate/users_dashboard_module8.html",username=username)
                  
    except Exception:
        return """<h1 style="color: red; text-align: center;">404 Page Not Found</h1>
            <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""



         