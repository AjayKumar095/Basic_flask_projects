from flask import Blueprint as bp, render_template, request,redirect, send_file
import os

module6_bp = bp('module6', __name__)

module6_bp.config['UPLOAD_FOLDER'] = '/path/to/your/uploads/folder'
module6_bp.config['MAX_CONTENT_LENGTH'] = 5 * 1024 * 1024  # 5 MB limit

ALLOWED_EXTENSIONS = {'txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'}

@module6_bp.route('/task6', methods=['POST'])
def task6():
    return render_template("module6_result.html")

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@module6_bp.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        # Handle case where no file is provided
        return redirect(request.url)

    file = request.files['file']

    if file.filename == '':
        # Handle case where no file is selected
        return redirect(request.url)

    if file and allowed_file(file.filename):
        # Delete the existing file (if it exists)
        existing_file_path = os.path.join(module6_bp.config['UPLOAD_FOLDER'], file.filename)
        if os.path.exists(existing_file_path):
            os.remove(existing_file_path)

        # Save the new file
        file.save(existing_file_path)

        return 'File uploaded successfully'

    # Handle invalid file type or size exceeds the limit
    return 'Invalid file type or size exceeds the limit'

@module6_bp.route('/view_uploaded_file/<filename>')
def view_uploaded_file(filename):
    file_path = os.path.join(module6_bp.config['UPLOAD_FOLDER'], filename)

    if allowed_file(filename):
        # Render content based on file type
        if filename.lower().endswith('.txt'):
            with open(file_path, 'r') as file:
                file_content = file.read()
        else:
            # Handle rendering for other file types (e.g., images, PDFs)
            return send_file(file_path, as_attachment=True)

        return render_template('uploaded_file_module6.html', file_content=file_content)

    # Handle invalid file type
    return 'Invalid file type'
