from flask import Blueprint as bp, render_template, request
import json
module4_bp = bp('module4', __name__)

@module4_bp.route('/task4', methods=['POST'])
def task4():
    return render_template("module4_result.html")

@module4_bp.route('/details', methods=['POST'])
def details():
    if request.method == 'POST':
        # Get details from the form
        name = request.form.get('name')
        age = request.form.get('age')
        email = request.form.get('email')
        details_dict = {'name': name, 'age': age, 'email': email}
        existing_details = []

        # Append the new details to the existing list
        existing_details.append(details_dict)
        with open('static/details.json', 'w') as json_file:
            json.dump(existing_details, json_file, indent=2)

        # Return the updated details to the HTML template
        return render_template('form_details_module4.html', details=existing_details)
    else:
        return f"Somthing went wrong."