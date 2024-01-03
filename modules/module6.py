from flask import Blueprint as bp, render_template, request
import os

module6_bp = bp('module6', __name__)

@module6_bp.route('/task6', methods=['GET','POST'])
def task6():
    return render_template("intermediate/module6_result.html")


@module6_bp.route('/upload', methods=['POST'])
def upload_file():
    folder_path="static"
    
    if 'file' not in request.files:
        return 'No file part'

    file = request.files['file']

    # If the user does not select a file, the browser sends an empty file
    if file.filename == '':
        return 'No selected file'

    # Check if the file is allowed based on its extension
    #if '.' in file.filename and file.filename.rsplit('.', 1)[1].lower()=='txt':
    if file.filename.endswith(".txt"):
    # Process the file (e.g., save it, get file information)
        file_name = file.filename
        file_path = os.path.join(folder_path, file.filename)
        file.save(file_path)
        with open(folder_path+"/"+file_name,'r') as f:
           content= f.read()
    
        os.remove(file_path)
    # Render the view_uploaded_file template with file information
        return render_template('intermediate/uploaded_file_module6.html', file_name=file_name,content=content)
    else:
        return 'Invalid file extension, file should be .txt extension.'