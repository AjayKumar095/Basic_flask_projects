from flask import Blueprint as bp, render_template, request, redirect, url_for
import logging
import json

logger = logging.getLogger(__name__)
module9_bp=bp("module9", __name__,static_folder='static')

@module9_bp.route('/task9', methods=["POST",'GET'])
def task9():
    return render_template("intermediate/module9_result.html")



# Method to add a new book in store.
@module9_bp.route("/add_books", methods=["POST",'GET'])
def add_books():
    if request.method=='POST':

        logger.info(f"form is valid")
        
        if 'add_book' in request.form:
            id=request.form.get("id")
            title=request.form.get("title")
            author=request.form.get("author")
            unit=request.form.get("unit")
            
            book={'id':id, "title":title,"Author":author, 'units':unit}
            add(book)
            #with open("static/book_data.json", 'r') as file:
               #logger.debug(f"file open as read mode")
               #data=json.load(file)
           # data.append(book)
            #with open("static/book_data.json", 'w') as file:
            
                #json.dump(data, file, indent=2)
               
            return redirect(url_for("module9.task9"))
        else:
            logger.info(f"form is not valid")
    else:
        logger.info(f"not enter in main if block")
    return redirect(url_for("module9.task9"))

# Method to display avaliable books.
@module9_bp.route("/display_books")     
def display_books():
    with open("static/book_data.json",'r') as file:
        book_data=json.load(file)
    return render_template("intermediate/bookData_modue9.html",book_data=book_data)

# Method to delete a book from the store by book id
@module9_bp.route("/delete_book")
def delete_book():
    pass

# Method to update the units of book by id.
@module9_bp.route("/update_unit", methods=["POST",'GET'])
def update_unit():
    
    if request.method=="POST":
        logger.info(f" enter in main if block")
        if 'update' in request.form:
            logger.info(f" enter in nested if block")
            global book_data
            book_id=request.form.get("id")
            new_unit=request.form.get("unit")
            
            for book in book_data:
                if book['id']==book_id:
                    book['units']==new_unit
                    logger.info(f"unit updated")
                    return redirect(url_for("module9.task9"))
                else:
                   return '<h1>The provided book id is not match with any record, please check you book id</h1>'    
        else:
            logger.info(f"not enter in nested if block")
            return '<h1>Internal server error</h1>'
    else:
        logger.info(f"not enter in main if block")
        return '<h1>Internal server error</h1>'

def add(book):
    with open("static/book_data.json", 'r') as file:
        logger.debug(f"file open as read mode")
        data=json.load(file)
     
    with open("static/book_data.json", 'w') as file:
        data.append(book)
        json.dump(data, file, indent=2)
    return None