# -*- coding: utf-8 -*-

from flask import Flask
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, TextAreaField
from wtforms.validators import Required, EqualTo
from flask import Flask, render_template, session, redirect, url_for, flash
import pymysql
app = Flask(__name__)

app.config['SECRET_KEY'] = 'that is a secret'
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql+pymysql://root:888888@localhost/blog'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)

class User(db.Model):
    __tablename__='users'
    username = db.Column(db.String(32), primary_key=True, index=True)
    password = db.Column(db.String(32))
    messages = db.relationship('Message', backref='user')

    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer,primary_key=True)
    username = db.Column(db.String(32), db.ForeignKey('users.username'), index=True)
    message = db.Column(db.String(512))

    def __repr__(self):
        return '用户名: %r ------ 留言: %r \n'  % (self.username, self.message)

class Log(FlaskForm):
    name = StringField('用户名', validators=[Required()])
    password = PasswordField('密码', validators=[Required()])
    submit = SubmitField('登录')

class Regist(FlaskForm):
    name = StringField('用户名', validators=[Required()])
    password1 = PasswordField('请输入密码', validators=[Required()])
    password2 = PasswordField('请再次输入密码', validators=[Required(), EqualTo('password1', message='两次密码必须相同')])
    submit = SubmitField('注册')

class Comment(FlaskForm):
    message = TextAreaField(validators=[Required()])
    submit = SubmitField('提交')

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = Log()
    if form.validate_on_submit():
        user = User.query.filter_by(username = form.name.data, password = form.password.data).first()
        if user is None:
            session['known'] = False
            flash('用户名或者密码错误')
        else:
            session['name'] = form.name.data
            session['password'] = form.password.data
            session['known'] = True
        return redirect(url_for('login'))
    return render_template('login.html', form=form, name=session.get('name', None), \
            known = session.get('known', False))

@app.route('/regist', methods=['GET', 'POST'])
def signin():
    form = Regist()
    if form.validate_on_submit():
        name = form.name.data
        password = form.password1.data
        user = User.query.filter_by(username = name).first()
        if user is None:
            user = User(username = name, password = password)
            db.session.add(user)
            flash('Success!')
        else:
            flash('该账户已注册!')
        return redirect(url_for('signin'))
    return render_template('regist.html', form=form)


@app.route('/', methods=['GET', 'POST'])
def home():
    form = Comment()
    if form.validate_on_submit():
        if session.get('name', None) != None:
            comment = form.message.data
            mess = Message(username = session.get('name'), message = comment)
            db.session.add(mess)
            flash('留言成功')
        else:
            flash('请先登录')
    messages = Message.query.all()
    return render_template('home.html', messages = messages, form = form)

if __name__ == '__main__':
    db.create_all()
    app.run()