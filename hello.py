from flask import Flask
from flask import render_template as rt
from flask import request, redirect, url_for
from db import insert, display,delete
app = Flask(__name__)
@app.route("/")
def helloGreet():
    return "Hello World"
@app.route("/ind",methods=["POST","GET"])
def home():
    if(request.method=='POST'):
        name=request.form["name"]
        email=request.form["email"]
        phone=request.form["phone"]
        insert(name,email,phone)
    return rt("index.html")
@app.route("/info")
def info():
    # c=0
    data=display()
    return rt("info.html",data=data)
@app.route("/delete/<int:id>")
def delet(id):
    delete(id)
    return redirect(url_for("info"))


