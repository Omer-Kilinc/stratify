from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, SelectField
from wtforms.validators import DataRequired

class CreateStrategyForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    asset_class = SelectField('Asset Class', validators=[DataRequired()], choices=[('Equities', 'Equities'), ('Crypto', 'Crypto'), ('Forex', 'Forex')])
    high_frequency = BooleanField('High Frequency')
