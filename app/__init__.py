from flask import Flask
import os
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

# app.config.from_object(os.environ['APP_SETTINGS'])
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)

from app import routes
