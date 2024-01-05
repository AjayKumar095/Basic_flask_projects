from flask import Blueprint as bp, render_template
module10_bp = bp('module10', __name__)

@module10_bp.route('/task10')
def task10():
    return render_template("intermediate/module10_result.html")

