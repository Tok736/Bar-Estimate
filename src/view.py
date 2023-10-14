from flask import render_template

from app import app

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ingredients")
def ingredients():
    return render_template("ingredients.html")

@app.route("/cocktails")
def cocktails():
    return render_template("cocktails.html")
