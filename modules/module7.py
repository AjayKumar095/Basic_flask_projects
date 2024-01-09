from flask import Blueprint as bp , render_template, redirect,url_for, request
import logging
import sqlite3

module7_bp=bp("module7", __name__)
logger = logging.getLogger(__name__)



@module7_bp.route('/task7', methods=["POST", "GET"])
def task7():
    try:
        return render_template("intermediate/module7_result.html")
    except Exception :
        return """<h1 style="color: red; text-align: center;">404 Page Not Found</h1>
                   <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""

    
# Method to add new book in database.
@module7_bp.route('/add', methods=['POST', "GET"])
def add():
    if request.method=="POST":
        if "add_book" in request.form:
            try:
                
                logger.info("Enter in if block")
                book_id=request.form.get("id")
                title=request.form.get("title")
                author=request.form.get("author")
                units=request.form.get("unit")
                with sqlite3.connect("static/module7_sqlite_database.db") as conn:
                    cursor=conn.cursor() 
                
                insert_statement = '''
                                INSERT INTO books (book_id, title, author,units )
                                VALUES (?, ?, ?, ?);
                            '''

                 # Execute the INSERT statement with the user input
                cursor.execute(insert_statement, (book_id, title, author,units))

               # Commit the changes and close the connection
                conn.commit()
                conn.close()
            
                return redirect(url_for("module7.task7"))
            
            except Exception:
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                        <h4 style="color: rgb(8, 8, 8); text-align: center;">Could not connect to database.</h4>
                        <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
        else:
            return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                   <h4 style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</h4>"""
    else:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""

# Method to display the book data      
@module7_bp.route("/display")
def display():
    
    try:
        
        with sqlite3.connect("static/module7_sqlite_database.db") as conn:
            cursor=conn.cursor() 
        
            select_statement = '''
                SELECT * FROM books;
            '''

            # Execute the SELECT statement
            cursor.execute(select_statement)

            # Fetch all rows as a list of tuples
            book_data = cursor.fetchall()
            conn.commit()
            conn.close()
        return render_template("intermediate/sqlite_data_module7.html", book_data=book_data)
    
    except Exception:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <h4 style="color: rgb(8, 8, 8); text-align: center;">Could not connect to database.</h4>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
        
@module7_bp.route("/update", methods=["POST", "GET"])
def update():
    if request.method=="POST":
        if "update" in request.form:
            
            try:
                book_id=request.form.get("id")
                new_unit=request.form.get("unit")
            
                with sqlite3.connect("static/module7_sqlite_database.db") as conn:
                    cursor=conn.cursor() 
                
                    update_statement = '''
                        UPDATE books
                        SET units = ?
                        WHERE book_id = ?;
                    '''
               
                    # Execute the UPDATE statement with the user input
                    cursor.execute(update_statement, (new_unit, book_id))
                    conn.commit()
                    conn.close()
                    return redirect(url_for("module7.task7"))
            
            except Exception:
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                        <h4 style="color: rgb(8, 8, 8); text-align: center;">Could not connect to database.</h4>
                        <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""    
        
        else:
            return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    else:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""

            
@module7_bp.route("/delete", methods=["POST", "GET"])
def delete():
    if request.method=="POST":
        if "delete" in request.form:
            
            try:
                
                book_id_to_delete=request.form.get("id")
                with sqlite3.connect("static/module7_sqlite_database.db") as conn:
                    cursor=conn.cursor()
                
                    delete_statement = '''
                        DELETE FROM books
                        WHERE book_id = ?;
                    '''

                    # Execute the DELETE statement with the user_id parameter
                    cursor.execute(delete_statement, (book_id_to_delete,))

                    # Commit the changes.
                    conn.commit()
                    return redirect(url_for("module7.task7"))
                
            except Exception:
                return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                        <h4 style="color: rgb(8, 8, 8); text-align: center;">Could not connect to database.</h4>
                        <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
        else:
            return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
    else:
        return """<h1 style="color: red; text-align: center;">500 Internal Server Error</h1>
                    <p style="color: rgb(8, 8, 8); text-align: center;">Sorry for any inconvenience. Our team is working hard to resolve the issue.</p>"""
           
                        