from flask import Flask, render_template, request
import pymysql
import pymysql.cursors
from pprint import pprint as print
xw


todolist = ["Go to sleep when im home", "Gaming", "Read books/comics"]

######

app = Flask(__name__)

######

@app.route("/", methods = ["GET", "POST"])
def index():
    if request.method == 'POST':
        newTodo = request.form["newTodo"]
        todolist.append(newTodo)

    return render_template ("todo.html.jinja", my2dolist = todolist )



@app.route("/delete_todo/<todo_index>", methods=['POST'])
def todo_delete(todo_index): 
    del todolist[todo_index]



 #return ("<p style=\"color:blue;\">Hello!</p>")