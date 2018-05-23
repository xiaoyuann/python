from flask import render_template, redirect, url_for, flash
from . import main
from .. import db
from .forms import CommentForm
from ..models import User, Message, load_user
from flask_login import current_user

@main.route('/', methods=['GET', 'POST'])
def home():
    form = CommentForm()
    if form.validate_on_submit():
        if current_user.is_authenticated:
            comment = form.message.data
            mess = Message(username = current_user.username, message = comment)
            db.session.add(mess)
            flash('Comment Success!')
        else:
            flash('Please log in first')
    messages = Message.query.all()
    return render_template('home.html', messages = messages, form = form)

