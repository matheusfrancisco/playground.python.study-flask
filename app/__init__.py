from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from flask_login import LoginManager


app = Flask(__name__)

app.config.from_object('config')
#UPLOAD_FOLDER = '/path/to/the/uploads'
#ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])

#app.config['SQLACHEMY_DATASABE_URI'] = 'sqlite:///storage.sb'

#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

db = SQLAlchemy(app)
migrate = Migrate(app,db)

manager = Manager(app) 
manager.add_command('db', MigrateCommand) 

lm = LoginManager()
lm.init_app(app)

from app.models import tables, forms
from app.controllers import default