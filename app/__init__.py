from flask import Flask, render_template, request
import socket
import mysql.connector

app = Flask(__name__)

@app.route('/')
def hello():
    # construct HTML output
    html = "<h3>Hello World from {hostname}!</h3>"
    html += "<h3>Your random word is: {random_word}</h3>"

    # yes, this is a terrible way to do this, but it works/is simple
    db = mysql.connector.connect(
              host=os.getenv("MYSQL_SERVICE_HOST"),
              port=os.getenv("MYSQL_SERVICE_PORT"),
              user="root",
              passwd=os.getenv("MYSQL_DB_PASSWORD"),
              database="randomizer",
              auth_plugin="mysql_native_password"
         )

    cursor = db.cursor()
    cursor.execute("select word from random_words order by rand() limit 1;")
    res = cursor.fetchall()

    return html.format(random_word=res[0][0], hostname=socket.gethostname())

@app.route('/index', methods=['GET', 'POST'])
def index():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']

        db = mysql.connector.connect(
              host=os.getenv("MYSQL_SERVICE_HOST"),
              port=os.getenv("MYSQL_SERVICE_PORT"),
              user="root",
              passwd=os.getenv("MYSQL_DB_PASSWORD"),
              database="randomizer",
              auth_plugin="mysql_native_password"
           )
        cursor = db.cursor()
        cursor.execute("INSERT INTO MyUsers(firstName, lastName) VALUES (%s, %s)", (firstName, lastName))  
#        cursor.execute("select word from random_words order by rand() limit 1;")
        res = cursor.fetchall()
#        return html.format(random_word=res[0][0], hostname=socket.gethostname())
    return render_template('index.html')
