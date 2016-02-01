from wtforms import Form, FloatField, validators
from math import pi

class InputForm(Form):
    A = FloatField(
        label='Sales', default=100,
        validators=[validators.InputRequired()])
    B = FloatField(
        label='Expense 1', default=1,
        validators=[validators.InputRequired()])
    C = FloatField(
        label='Expense 2', default=1,
        validators=[validators.InputRequired()])
    D = FloatField(
        label='Expense 3', default=1,
        validators=[validators.InputRequired()])
    E = FloatField(
        label='Expense 4', default=1,
        validators=[validators.InputRequired()])
    F = FloatField(
        label='Expense 5', default=1,
        validators=[validators.InputRequired()])
