from app import app
from flask import Flask, render_template

@app.route('/')
def welcome():
    return render_template("index.html")
