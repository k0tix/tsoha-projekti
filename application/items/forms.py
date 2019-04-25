from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, SelectField
from wtforms.validators import AnyOf, InputRequired

values = ["Legendary", "Super", "Rare", "Uncommon", "Common"]

class ItemForm(FlaskForm):
    name = StringField("name", validators=[InputRequired("Item must have a name")])
    price = IntegerField("price", validators=[InputRequired("Item must have a price")])
    quality = FloatField("quality", validators=[InputRequired("Item must have a quality value")])
    item_type = SelectField(label="type", choices=[(c, c) for c in values], validators=[AnyOf(values, "Value must be Legendary, Super, Rare, Uncommon or Common")])

    class Meta:
        csrf = False