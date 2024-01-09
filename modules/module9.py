from flask import Blueprint as bp, render_template, request, redirect, url_for
import logging
import json

logger = logging.getLogger(__name__)
module9_bp=bp("module9", __name__)

@module9_bp.route('/task9', methods=["POST",'GET'])
def task9():
    try:
        return render_template("intermediate/module9_result.html")
    
    except Exception:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""


# Method to add a new book in store.
@module9_bp.route("/add_books", methods=["POST",'GET'])
def add_books():
    if request.method=='POST': # Chacking for valid method
        logger.info("enter in main if")
        if 'add_book' in request.form:
            logger.info("enter in  nested if")
            Id=request.form.get("id")
            Title=request.form.get("title")
            author=request.form.get("author")
            Unit=request.form.get("unit")
            
            book={'id':(Id), "title":Title,"Author":author, 'units':(Unit)}
            logger.info(f"before file open as read mode")
            
            try:
                with open("static/book_data.json", 'r') as file: # open file for reading.
                   logger.info(f"file open as read mode")
                   data=json.load(file)
           
                with open("static/book_data.json", "w") as file: # Appending new data to file.
                    data.append(book)
                    json.dump(data, file, indent=2)
                file.close()   # closing file after use
                return redirect(url_for("module9.task9")) # redirecting to home page
            
            except FileNotFoundError: # Exception handling
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""   
        else:
            logger.info("form is not valid")
    else:
        logger.info("not enter in main if block")
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""

# Method to display avaliable books.
@module9_bp.route("/display_books")     
def display_books():
    try:
        with open("static/book_data.json",'r') as file: # open file for reading.
            book_data=json.load(file)
        return render_template("intermediate/bookData_modue9.html",book_data=book_data)
    
    except FileNotFoundError:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    
# Method to delete a book from the store by book id
@module9_bp.route("/delete_book", methods=["POST",'GET'])
def delete_book():
    
    if request.method=='POST': # Chacking for valid method
        if 'delete' in request.form:
            try: 
                with open('static/book_data.json', 'r') as file: # open file for reading.
                   data = json.load(file)
                get_id=request.form.get("Id")
                for item in data:         # removing book data from file
                    if item['id'] == int(get_id):
                        data.remove(item)
                        break  

                with open('static/book_data.json', 'w') as file:  # updating file
                    json.dump(data, file, indent=2)
                file.close()  
                   
            except FileNotFoundError : # Exception handling
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
                
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    else:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    
    
# Method to update the units of book by id.
@module9_bp.route("/update_unit", methods=["POST",'GET'])
def update_unit():
    
    if request.method=="POST": # Chacking for valid method
        logger.info(f" enter in main if block")
        if 'update' in request.form:
            logger.info(f" enter in nested if block")
            try:
                with open("static/book_data.json", 'r') as file: # open file for reading.
                   logger.info(f"file open as read mode")
                   data=json.load(file)
                book_id=request.form.get("Id")
                new_unit=request.form.get("Unit")
                for book in data:  # updating data by for loop
                    try:
                        if book['id']==int(book_id):
                            book['units']=int(new_unit)
                            with open("static/book_data.json", "w") as file: # Updating data
                                json.dump(data, file, indent=2) 
                            file.close()    
                            break    
                    except Exception as e: # Exception handling
                       return f'Book id must be integer {e}'
                   
            except FileNotFoundError: # Exception handling
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""     
                    
            return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""  # redirecting to home page
        else:
            logger.info(f"not enter in nested if block")
            
            return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    else:
        logger.info(f"not enter in main if block")
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
