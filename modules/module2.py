# module2.py
from flask import Blueprint as bp, render_template, request

module2_bp = bp('module2', __name__)

@module2_bp.route('/task2', methods=['POST'])
def task2():
    result = "Welcome!"
    return render_template("module2_result.html", result=result)

@module2_bp.route('/page1')
def page1():
    return render_template('page1_module1.html')

@module2_bp.route('/home')
def home():
    return render_template("module2_result.html")