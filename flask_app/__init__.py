# this file is where you import Flask and session
from flask import Flask, session
from flask_bcrypt import Bcrypt

app = Flask(__name__)
app.secret_key = "secretsauce"

bcrypt = Bcrypt(app)

DATABASE = "login_and_registration"