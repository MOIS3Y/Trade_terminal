from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from app import db
# from app import login

users_exchanges = db.Table(
    'users_exchanges',
    db.Column('id', db.Integer, primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('exchange_id', db.Integer, db.ForeignKey('exchange.id')),
    db.Column('secret_key', db.String(128), db.ForeignKey('user.id')),
    db.Column('public_key', db.String(128), db.ForeignKey('user.id'))
    )


class User(UserMixin, db.Model):
    """docstring for User"""
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    exchanges = db.relationship(
        'Exchange', secondary=users_exchanges, backref=db.backref(
            'users', lazy='dynamic'))

    def __repr__(self):
        return '<User {}>'.format(self.login)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Exchange(db.Model):
    """docstring for Post"""
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

    def __repr__(self):
        return '<Exchange {}>'.format(self.name)


class PrivatSettings(db.Model):
    """docstring for Post"""
    id = db.Column(db.Integer, primary_key=True)
    secret_key = db.Column(db.String(128))
    public_key = db.Column(db.String(128))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

#     def __repr__(self):
#         return '<User {}, Exchange {}>'.format(self.user_id, self.name_id)
# @login.user_loader
# def load_user(id):
#     return User.query.get(int(id))
