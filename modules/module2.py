# module2.py
from flask import Blueprint as bp, render_template, request

module2_bp = bp('module2', __name__)

@module2_bp.route('/task2', methods=['POST'])
def task2():
    return render_template("basic/module2_result.html")

@module2_bp.route('/page1')
def page1():
    return render_template('basic/page1_module2.html')

@module2_bp.route('/home')
def home():
    return render_template("basic/module2_result.html")