from flask import render_template, redirect, url_for, flash
from .forms import LogForm, SignForm
from . import auth
from .. import db
from ..models import User
from flask_login import login_user, login_required, logout_user, current_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LogForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user is not None and user.verify_passwd(form.passwd.data):
            login_user(user, form.remeber_me.data)
            flash('Log In Success')
            return redirect(url_for('main.home'))
        else:
            flash('email or password is error')
            return redirect(url_for('auth.login'))
    return render_template('auth/login.html', form=form)

@auth.route('/signin', methods=['GET', 'POST'])
def signin():
    form = SignForm()
    if form.validate_on_submit():
        name = form.name.data
        passwd = form.passwd1.data
        email = form.email.data
        user = User(username = name, passwd = passwd, email = email)
        db.session.add(user)
        flash('Success!')
        return redirect(url_for('auth.login'))
    return render_template('auth/signin.html', form=form)



@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have been logged out')
    return redirect(url_for('main.home'))
