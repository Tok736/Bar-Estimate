from flask import render_template

from app import app
from models import Ingredient

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ingredients")
def ingredients():
    ingredient_list = Ingredient.query.all()
    return render_template("ingredients.html", enumerated_ingredient_list=enumerate(ingredient_list))

@app.route("/cocktails")
def cocktails():
    return render_template("cocktails.html")
