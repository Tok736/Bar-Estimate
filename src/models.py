from db import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_group = db.Column(db.String(100))
    name = db.Column(db.String(100), unique=True)
    permalink = db.Column(db.String(100), unique=True)

    def __repr__(self):
        return f"<{self.ingredient_group} - {self.name}>"
