from flask import Blueprint as bp, render_template

module3_bp = bp('module3', __name__)

@module3_bp.route('/task3', methods=['POST'])
def task3():
    return render_template("basic/module3_result.html")

@module3_bp.route('/person/<int:id>')
def person_details(id):
     person_data = {
        1: {'name': 'John Doe', 'age': 30, 'occupation': 'Engineer'},
        2: {'name': 'Jane Smith', 'age': 25, 'occupation': 'Designer'},
        3: {'name': 'Michael Johnson', 'age': 35, 'occupation': 'Teacher'},
        4: {'name': 'Emily Davis', 'age': 28, 'occupation': 'Doctor'},
        5: {'name': 'Christopher White', 'age': 40, 'occupation': 'Programmer'},
    }
     
     person=person_data.get(id)
     return render_template('basic/person_details.html', person=person)