from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
from app import login


class User(UserMixin, db.Model):
    """docstring for User"""
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    private_settings = db.relationship(
        'PrivateSettings', backref=db.backref('users'), lazy=True)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Exchange(db.Model):
    """docstring for Exchange"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128), index=True, unique=True)
    private_settings = db.relationship(
        'PrivateSettings', backref=db.backref('exchange'), lazy=True)

    def __repr__(self):
        return '<Exchange {}>'.format(self.name)


class PrivateSettings(db.Model):
    """docstring for PrivateSettings"""
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    exchange_id = db.Column(db.Integer, db.ForeignKey('exchange.id'))
    name = db.Column(db.String(12))
    secret_key = db.Column(db.String(128))
    public_key = db.Column(db.String(128))

    def __repr__(self):
        return '<User: {}, Exchange:{}, SK: {}, PK: {}, Name: {}>'.format(
            self.user_id, self.exchange_id,
            self.secret_key, self.public_key,
            self.name)


@login.user_loader
def load_user(id):
    return User.query.get(int(id))
