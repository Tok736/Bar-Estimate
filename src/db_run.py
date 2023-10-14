from db import db
from app import app
from models import Ingredient

with app.app_context():
    db.drop_all()
    db.create_all()

with app.app_context():
    ingredients = [
        Ingredient(ingredient_group="Кисло-сладкий баланс", name="Сок лимона"),
        Ingredient(ingredient_group="Кисло-сладкий баланс", name="Сок лайма")
    ]

    for i in ingredients:
        db.session.add(i)

    db.session.commit()


# with app.app_context():
#     doctors = Doctor.query.all()
#     print(doctors)

