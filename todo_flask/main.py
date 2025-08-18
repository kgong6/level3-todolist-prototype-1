from flask import Flask, session, render_template, request, g, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

import sqlite3, random,




app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db= SQLAlchemy(app)

class Todo(db.Model):
    task_id=db.Column(db.Integer,primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    done=db.Column(db.Boolean, default=False)

def __init__(self, name: str, done: bool = False):
    self.name = name
    self.done = done

with app.app_context():
    db.create_all()


@app.route("/", methods=["POST", "GET"])
def index():
    todo_list=Todo.query.all()
    session["all_items"], session["todo_items"] = get_db()
    return render_template("index.html", 
                           todo_list=todo_list,
                           all_items= session["all_items"],
                           todo_items= session["todo_items"])

#For where the user writes their own tasks
@app.route('/add', methods=['POST'])
def add():
    name=request.form.get("name")
    new_task= Todo(name = name, done = False) # type: ignore
    db.session.add(new_task)
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/update/<int:todo_id>')
def update(todo_id):
    todo = Todo.query.get_or_404(todo_id)
    todo.done = not todo.done
    db.session.commit()
    return redirect(url_for("index"))

@app.route('/delete/<int:todo_id>')
def delete(todo_id):
    todo=Todo.query.get(todo_id)
    db.session.delete(todo)
    db.session.commit()
    return redirect(url_for("index"))


#for suggested tasks add button
@app.route("/add_items", methods = ["POST"])
def add_items():
    session["todo_items"].append(request.form["select_items"])
    session.modified = True
    return render_template("index.html", 
                           all_items= session["all_items"], 
                           todo_items= session["todo_items"]) 

#for suggested tasks remove button
@app.route("/remove_items", methods = ["POST"])
def remove_items():
    checked_boxes = request.form.getlist("check")

    for item in checked_boxes:
        if item in session["todo_items"]:
            idx= session["todo_items"].index(item)
            session["todo_items"].pop(idx)
            session.modified = True
            
    return render_template("index.html", 
           all_items= session["all_items"], 
           todo_items= session["todo_items"])

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db=g._database = sqlite3.connect('todo_list.db')
        cursor = db.cursor()
        cursor.execute("select name from tasks")
        all_data = cursor.fetchall()
        all_data = [str(val[0]) for val in all_data]

        todo_list = all_data.copy()
        random.shuffle(todo_list)
        todo_list = todo_list[:3]
    
    return all_data, todo_list # type: ignore
    

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=5000)
