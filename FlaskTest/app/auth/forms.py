from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField, BooleanField
from wtforms.validators import Required, EqualTo, Email, Length, Regexp
from wtforms import ValidationError
from ..models import User

class LogForm(FlaskForm):
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    passwd = PasswordField('Password', validators=[Required()])
    remeber_me = BooleanField('Keep me logged in')
    submit = SubmitField('Log In')

class SignForm(FlaskForm):
    name = StringField('Username', validators=[Required(), Length(1, 64), \
                        Regexp('^[A-Za-z][A-Za-z0-9_.]*$', 0, \
                        'Usernames must have only letters,numbers, dots or underscores')])
    email = StringField('Email', validators=[Required(), Email(), Length(1, 64)])
    passwd1 = PasswordField('Password', validators=[Required()])
    passwd2 = PasswordField('Comfirm Password', \
            validators=[Required(), EqualTo('passwd1', message='Passwords must be match')])
    submit = SubmitField('Sign In')

    def validate_email(self, field):
        if User.query.filter_by(email = field.data).first():
            raise ValidationError('Email already registered.')

    def validate_username(self, field):
        if User.query.filter_by(username = field.data).first():
            raise ValidationError('Username already in use')