from flask_smorest import Blueprint

bp = Blueprint('specs', __name__, description="Operations for specs")

from . import routes