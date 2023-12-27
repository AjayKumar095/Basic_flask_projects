from flask import blueprints as bp, render_template

module6_bp=bp('module6',__name__)

@module6_bp.route('task6', methods=['POST'])
def task6():
    result='program 6'
    return render_template('module6_result.html', result=result)