from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager

from config import Config

app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)
jwt = JWTManager(app)

from models.cars_model import CarsModel
from models import SpecsModel, CarsModel

from resources.cars import bp as cars_bp
api.register_blueprint(cars_bp)

from resources.specs import bp as specs_bp
api.register_blueprint(specs_bp)