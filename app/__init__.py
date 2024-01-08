from flask import Flask

from config import Config


app = Flask(__name__)
app.config.from_object(Config)


from resources.specs import bp as specs_bp
app.register_blueprint(specs_bp)


from resources.cars import bp as cars_bp
app.register_blueprint(cars_bp)