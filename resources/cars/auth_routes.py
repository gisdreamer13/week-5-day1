from flask_jwt_extended import create_access_token

from models import CarsModel

from . import bp 
from schemas import CarsLogin

@bp.post('/login')
@bp.arguments(CarsLogin)
def login(cars_data):
  cars = CarsModel.query.filter_by(username = cars_data['username']).first()
  if cars and cars.check_password(cars_data['password']):
    access_token = create_access_token(cars.id)
    return {'token': access_token}
  return {'message': 'Invalid user data'}