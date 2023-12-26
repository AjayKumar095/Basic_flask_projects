from flask import Blueprint as bp, render_template

module5_bp = bp('module5', __name__)

@module5_bp.route('/task5', methods=['POST'])
def task5():
    result = "amazing"
    return render_template("module5_result.html",result=result)