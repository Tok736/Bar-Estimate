from db import db

class Ingredient(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    ingredient_group = db.Column(db.String(100), nullable=False)
    name = db.Column(db.String(100))

    def __repr__(self):
        return f"<{self.ingredient_group} - {self.name}>"
