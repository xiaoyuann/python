from flask_wtf import FlaskForm
from wtforms import SubmitField, TextAreaField
from wtforms.validators import Required

class CommentForm(FlaskForm):
    message = TextAreaField(validators=[Required()])
    submit = SubmitField('Comment')
