from flask_smorest import Blueprint

bp = Blueprint('Cars', __name__, description="Operations for Cars")

from . import routes, auth_routes