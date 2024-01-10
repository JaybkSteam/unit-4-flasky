from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print

conn = pymysql.connect (
    database="jedouard_todos",
    user="jedouard",
    password="224449553",
    host="10.100.33.60",
    cursorclass=pymysql.cursors.DictCursor
)

todolist = ["Go to sleep when im home", "Gaming", "Read books/comics"]

######

app = Flask(__name__)

######

@app.route("/", methods = ["GET", "POST"])
def index():

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`") #DESC to reverse the order

    cursor.close()

    conn.commit()

    if request.method == 'POST':
        newTodo = request.form["newTodo"]
        todolist.append(newTodo)

        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{newTodo}'")
        
        cursor.close()

        conn.commit()

    return render_template ("todo.html.jinja", my2dolist = todolist )



@app.route("/delete_todo/<todo_index>", methods=['POST'])
def todo_delete(todo_index): 
   # del todolist[todo_index]

    cursor = conn.cursor()

    cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{todo_index}'")

    cursor.close()

    conn.commit()

    return redirect("/")






 #return ("<p style=\"color:blue;\">Hello!</p>")