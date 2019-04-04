from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField

class ItemForm(FlaskForm):
    name = StringField("name")
    price = IntegerField("price")
    quality = FloatField("quality")
    item_type = StringField("type")

    class Meta:
        csrf = False