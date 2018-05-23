from . import db, login_manager
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), unique=True, index=True)
    email = db.Column(db.String(64), unique=True, index=True)
    passwd_hash = db.Column(db.String(128))
    messages = db.relationship('Message', backref='user')

    @property
    def passwd(self):
        raise AttributeError('password is not a readable attribute')

    @passwd.setter
    def passwd(self, passwd):
        self.passwd_hash = generate_password_hash(passwd)
    
    def verify_passwd(self, passwd):
        return check_password_hash(self.passwd_hash, passwd)
        
    def __repr__(self):
        return '<User %r>' % self.username

class Message(db.Model):
    __tablename__ = 'messages'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), db.ForeignKey('users.username'), index=True)
    message = db.Column(db.String(256))

    def __repr__(self):
        return 'User: %r \n Message: %r \n'  % (self.username, self.message)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
