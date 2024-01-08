from flask import Blueprint as bp , render_template, redirect,url_for, request
import logging
import sqlite3

module7_bp=bp("module7", __name__)
logger = logging.getLogger(__name__)

conn=sqlite3.connect("static/module7_sqlite_database.db")
cursor=conn.cursor()

@module7_bp.route('/task7', methods=["POST", "GET"])
def task7():
    return render_template("intermediate/module7_result.html")


@module7_bp.route('/add', methods=['POST', "GET"])
def add():
    if request.method=="POST":
        if "add_book" in request.form:
            logger.info("Enter in if block")
            book_id=request.form.get("id")
            title=request.form.get("title")
            author=request.form.get("author")
            units=request.form.get("unit")
            
            insert_statement = '''
                            INSERT INTO users (username, email, birthdate)
                            VALUES (?, ?, ?,?);
                        '''

             # Execute the INSERT statement with the user input
            cursor.execute(insert_statement, (book_id, title, author,units))

           # Commit the changes and close the connection
            conn.commit()
            conn.close()
            
            return redirect(url_for("module7.task7"))
        else:
            return "error"