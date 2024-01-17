from flask import request

from flask.views import MethodView
from flask_jwt_extended import get_jwt_identity, jwt_required
from flask_smorest import abort
from . import bp

from schemas import CarsSchema, CarsSchemaNested
from models.cars_model import CarsModel
# user routes

@bp.route('/cars/<cars_id>')
class User(MethodView):

  @bp.response(200, CarsSchemaNested)
  def get(self,cars_id):
    cars = CarsModel.query.get(cars_id)
    if cars:
      print(cars.posts.all())
      return cars
    else:
      abort(400, message='Cars not found')

  @jwt_required()  
  @bp.arguments(CarsSchema)
  def put(self, cars_data, cars_id):
    cars = CarsModel.query.get(get_jwt_identity())
    if cars and cars.id == cars_id:
      cars.from_dict(cars_data)
      cars.commit()
      return { 'message': f'{cars.username} updated'}, 202
    abort(400, message = "Invalid Car")

  @jwt_required()
  def delete(self, cars_id):
    cars = CarsModel.query.get(get_jwt_identity())
    if cars == cars_id:
      cars.delete()
      return { 'message': f'User: {cars.username} Deleted' }, 202
    return {'message': "Invalid car"}, 400

@bp.route('/cars')
class CarsList(MethodView):

  @bp.response(200, CarsSchema(many = True))
  def get(self):
   return CarsModel.query.all()
  
  @bp.arguments(CarsSchema)
  def post(self, cars_data):
    try:
      cars = CarsModel()
      cars.from_dict(cars_data)
      cars.commit()
      return { 'message' : f'{cars_data["model"]} created' }, 201
    except:
      abort(400, message='Username and Email Already taken')
      
@bp.route('/cars/follow/<followed_id>')
class FollowUser(MethodView):

  @jwt_required()
  def post(self, followed_id):
    followed = CarsModel.query.get(followed_id)
    follower =CarsModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.follow(followed)
      followed.commit()
      return {'message':'cars followed'}
    else:
      return {'message':'invalid user'}, 400
  @jwt_required()  
  def put(self, followed_id):
    followed = CarsModel.query.get(followed_id)
    follower = CarsModel.query.get(get_jwt_identity())
    if follower and followed:
      follower.unfollow(followed)
      followed.commit()
      return {'message':'cars unfollowed'}
    else:
      return {'message':'invalid user'}, 400