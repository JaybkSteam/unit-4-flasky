from flask import Flask, render_template, request, redirect
import pymysql
import pymysql.cursors
from pprint import pprint as print
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash


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
auth = HTTPBasicAuth()

######

users = {
    "jayroc": generate_password_hash("pokemon123"),
    "1206": generate_password_hash("gottacatch1")
}


@auth.verify_password
def verify_password(username, password):
    if username in users and \
            check_password_hash(users.get(username), password):
        return username


@app.route("/", methods = ["GET", "POST"])
@auth.login_required
def index():

    if request.method == 'POST':
        newTodo = request.form["newTodo"]
        todolist.append(newTodo)

        cursor = conn.cursor()

        cursor.execute(f"INSERT INTO `todos` (`description`) VALUES ('{newTodo}')")
        
        cursor.close()

        conn.commit()
    
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM `todos` ORDER BY `complete`") #DESC to reverse the order

    results = cursor.fetchall()

    cursor.close()

    return render_template ("todo.html.jinja", my2dolist = results )

    return "Hello, {}!".format(auth.username())



@app.route("/delete_todo/<todo_index>", methods=['POST'])
def todo_delete(todo_index): 
   # del todolist[todo_index]

    cursor = conn.cursor()

    cursor.execute(f"DELETE FROM `todos` WHERE `id` = {todo_index}")

    cursor.close()

    conn.commit()

    return redirect("/")






 #return ("<p style=\"color:blue;\">Hello!</p>")
