from flask import Blueprint as bp, render_template

module3_bp = bp('module3', __name__)

@module3_bp.route('/task3', methods=['POST'])
def task3():
    result = "Python Programming"
    return render_template("module3_result.html",result=result)