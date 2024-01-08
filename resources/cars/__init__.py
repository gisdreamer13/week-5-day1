from flask_smorest import Blueprint

bp = Blueprint('cars', __name__, description="Ops on Cars", url_prefix='/car')

from . import routes