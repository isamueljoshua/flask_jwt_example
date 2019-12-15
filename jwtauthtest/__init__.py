from flask import Flask
from jwtauthtest.database import init_db, shutdown_db_session
# from os import environ

app = Flask(__name__)
# app.config['SECRET_KEY'] = environ.get('JWT_SECRET_KEY')

# decorator registers a function to be called when the flask application context ends
@app.teardown_appcontext
def shutdown_session(exception=None):
    shutdown_db_session()


init_db()

import jwtauthtest.jwt
import jwtauthtest.views