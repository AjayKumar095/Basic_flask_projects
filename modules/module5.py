from flask import Blueprint as bp, render_template, redirect, url_for, session,request

module5_bp = bp('module5', __name__)

@module5_bp.route('/task5', methods=['GET','POST'])
def task5():
   if 'username' in session:
        username = session['username']
        return render_template('basic/user_module5.html', username=username)
   else:
        return render_template('basic/module5_result.html')

@module5_bp.route('/login', methods=['POST'])
def login():
    # Get the username from the form
    username = request.form.get('username')

    # Store the username in the session
    session['username'] = username

    return redirect(url_for('module5.task5'))

@module5_bp.route('/logout', methods=['GET', 'POST'])
def logout():
    # Remove 'username' from the session
    session.pop('username')
    return redirect(url_for('module5.task5'))

