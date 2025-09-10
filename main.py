from flask import Flask, session, render_template, request, g

import sqlite3, random

app = Flask(__name__)
app.secret_key = "iuu78iuytu765kukjngdtrwivukctjn"
app.config["SESSION_COOKIE_NAME"] = "tfi7865jkhugyutfdt53w4q4ygbctshxro"


# Home page route
@app.route("/", methods=["POST", "GET"])
def index():
    session["all_items"], session["todo_items"] = get_db()
    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])


@app.route("/add_items", methods=["POST"])
def add_items():
    """
    Adds a selected item to the 'todo_items' list.
    It then re-renders to show the updated list.
    """
    session["todo_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])


@app.route("/remove_items", methods=["POST"])
def remove_items():
    """
    Removes selected items from the 'todo_items' list and updates.
    It then re-renders to display the updated list.
    """
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["todo_items"]:
            idx = session["todo_items"].index(item)
            session["todo_items"].pop(idx)
            session.modified = True

    return render_template("index.html",
                           all_items=session["all_items"],
                           todo_items=session["todo_items"])


'''Connects to the 'todo_list.db' SQLite database, retrieves a list of tasks,
and shuffles the list to select three random tasks.'''


def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('todo_list.db')
        cursor = db.cursor()
        cursor.execute("select name from tasks")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        todo_list = all_data.copy()
        random.shuffle(todo_list)
        todo_list = todo_list[:3]

    return all_data, todo_list


#Closes the database connection at the end.


@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=False)
