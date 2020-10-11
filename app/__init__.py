from flask import Flask, render_template, request
import os, socket
import mysql.connector

app = Flask(__name__)

# DB initialization
db = mysql.connector.connect(
              host=os.getenv("MYSQL_SERVICE_HOST"),
              port=os.getenv("MYSQL_SERVICE_PORT"),
              user="root",
              passwd=os.getenv("MYSQL_ROOT_PASSWORD"),
              database="PARADB",
              auth_plugin="mysql_native_password"
)

@app.route('/init')
def init():
    cursor = db.cursor()
    cursor.execute("DROP DATABASE IF EXISTS PARADB")
    cursor.execute("CREATE DATABASE PARADB")
    cursor.execute("USE PARADB")
    sql = """CREATE TABLE users (
         fname char(20),
         lname char(20)
     )"""
    cursor.execute(sql)
    db.commit()
    return "DB Init done" 

@app.route('/getusers')
def getusers():
    cursor = db.cursor()
    cursor.execute("select * from users;")
    data = cursor.fetchall()

    return render_template("example.html", title='User Data', value=data)

@app.route('/addusers', methods=['GET', 'POST'])
def addusers():
    if request.method == "POST":
        details = request.form
        firstName = details['fname']
        lastName = details['lname']

        cursor = db.cursor()
        cursor.execute("INSERT INTO PARADB.users (fname, lname) VALUES (%s, %s)", (firstName, lastName))
        db.commit() 
#        cursor.execute("select * from MyUsers;") 
#        data = cursor.fetchall()
    return render_template('index.html', message="Users Added!")
