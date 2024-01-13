from flask_smorest import Blueprint

bp = Blueprint('specs', __name__, description='Ops on Specs', url_prefix='/specs')

from . import routes