from flask import Blueprint as bp, render_template
module10_bp = bp('module10', __name__)

@module10_bp.route('/task10',methods=['POST'])
def task10():
    return render_template("intermediate/module10_result.html")

@module10_bp.route('handling404')
def handling404():
    
    try:
       # The text file we try no open does not exist, hence it give a 404 error.
       with open("xyz.txt",'r') as f:
           data=f.read()
       return data
    except Exception as e:
        return render_template("intermediate/error_404_module10.html", e=e)

@module10_bp.route('handling500')
def handling500():
    try:
        # Here we try to devide 1 by 0 which is mathamaticaly not possible, Hence it give a 500 error.
        result=1/0
        return result
    except ZeroDivisionError as e:
        return render_template("intermediate/error_500_module10.html",e=e)
    
@module10_bp.route('/home') 
def home():
    return render_template('index.html')   

    