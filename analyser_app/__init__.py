from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import relation, relationship

app = Flask(__name__)

'''
While developing the app these are set statically however in a production 
environment these should be set as environment variables and accessed using the 
Config class pattern:

-- structure --
app/
    __init__.py
    config.py

--- import for init.py --
from app.config import Config

--- config.py ---
class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('SQLALCHEMY_DATABASE_URI')

'''
app.config["SECRET_KEY"] = "ca6c67f3c64230cd3410198b4316dcbf"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///site.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True # development only

# db needs to exist for the models module
db = SQLAlchemy(app)

# leave this import here - prevents circular import issues
from analyser_app import routes