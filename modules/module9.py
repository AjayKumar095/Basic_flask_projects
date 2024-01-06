from flask import Blueprint as bp, render_template

module9_bp=bp("module9", __name__)

@module9_bp.route('test9', methods=["POSt"])
def test9():
    result='Hello'
    return render_template("intermediate/module9_result.html", result=result)