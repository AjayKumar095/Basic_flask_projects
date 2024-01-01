from flask import Blueprint as bp, render_template

module11_bp = bp('module11', __name__)

@module11_bp.route('/task3', methods=['POST'])
def task11():
    res="hello"
    return render_template("module11_result.html", res=res)