# module1.py
from flask import Blueprint as bp, render_template

module1_bp = bp('module1', __name__)

@module1_bp.route('/task1', methods=['POST'])
def task1():
    result = "Hello, World!"
    return render_template("basic/module1_result.html",result=result)
