from flask import Flask
from flask_smorest import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


from config import Config


app = Flask(__name__)
app.config.from_object(Config)
api = Api(app)

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from models.cars_model import CarsModel
from models.SpecsModel import SpecsModel



from resources.specs import bp as specs_bp
api.register_blueprint(specs_bp)


from resources.cars import bp as cars_bp
api.register_blueprint(cars_bp)