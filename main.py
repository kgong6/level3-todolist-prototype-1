# Features : dropdown task selection, todo list, bunny illustration progress indicator.

from flask import Flask, session, render_template, request, g

import sqlite3, random

# Create Flask app
app = Flask(__name__)

# Secret key for security
app.secret_key = "iuu78iuytu765kukjngdtrwivukctjn"
app.config["SESSION_COOKIE_NAME"] = "tfi7865jkhugyutfdt53w4q4ygbctshxro"


# Main page - shows gif, todo list, and dropdown.
@app.route("/", methods=["POST", "GET"])
def index():
    # Get all wellbeing tasks and current todolist from database
    session["all_items"], session["todo_items"] = get_db()
    # Display main page with both lists
    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])


# Adds wellbeing tasks from dropdown to todolist
@app.route("/add_items", methods=["POST"])
def add_items():
    
    session["todo_items"].append(request.form["select_items"])
    session.modified = True

    # Shows updated page with new task added
    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])

# Remove completed tasks from todo list
@app.route("/remove_items", methods=["POST"])
def remove_items():
   # Get all checked tasks from the form
    checked_boxes = request.form.getlist("check")

    # Remove each checked task from todo list
    for item in checked_boxes:
        if item in session["todo_items"]:
            # Find and remove the completed task
            idx = session["todo_items"].index(item)
            session["todo_items"].pop(idx)
            session.modified = True
            
    # Show updated page 
    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])



def get_db():
    '''
    Connects to the 'todo_list.db' SQLite database of wellbeing tasks. 
    Gets all available tasks + 3 random tasks for todo list.
    '''
    
    db = getattr(g, '_database', None)
    if db is None:
        
        # Connect to database
        db = g._database = sqlite3.connect('todo_list.db')
        cursor = db.cursor()
        
        # Get all task names
        cursor.execute("select name from tasks")
        all_data = cursor.fetchall()
        
        all_data = [str(val[0]) for val in all_data]

        # Create todolist with 3 random tasks
        todo_list = all_data.copy()
        random.shuffle(todo_list)
        todo_list = todo_list[:3]

    return all_data, todo_list


# Closes the database connection at the end.
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

# Run app
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
