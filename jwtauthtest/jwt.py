# handles the process of token generation, decoding and signing for us.
from flask_jwt import JWT
from jwtauthtest import app
from jwtauthtest.models import User
from passlib.hash import pbkdf2_sha256
# from os import environ


def authenticate(username, password):
    user = User.query.filter_by(username=username).first()
    if user and pbkdf2_sha256.verify(password, user.password):
        return user


def identity(payload):
    user_id = payload['identity']
    return User.query.get(user_id)


# app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')
# Give a custom Secret key, the above code didn't work
app.config['SECRET_KEY'] = 'Secseccc'
jwt = JWT(app, authenticate, identity)