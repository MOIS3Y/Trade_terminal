from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms import SelectField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('User name:', validators=[DataRequired()])
    password = PasswordField('Password:', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')


class SettingsForm(FlaskForm):
    """docstring for EditProfileForm"""
    select = SelectField('Exchanges', choices=[], coerce=int)
    name = StringField('Name:', validators=[DataRequired()])
    secret_key = StringField('Secret key:', validators=[DataRequired()])
    public_key = StringField('Public key:', validators=[DataRequired()])
    submit = SubmitField('Add')

# form = SettingsForm()
# form.select.choices =[(exchange.id, exchange.name) for exchange in exchanges]
# flash(form.select.choices)
