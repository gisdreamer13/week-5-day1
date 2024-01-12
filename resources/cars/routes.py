from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models.cars_model import CarsModel
from schemas import CarsSchema
from db import specs, cars
from . import bp



@bp.route('/car/<car_id>')
class Cars(MethodView):
    
    @bp.response(200, CarsSchema)
    def get(self, car_id):
        cars = CarsModel.query.get(car_id)
        if cars:
            return cars
    abort(400, message = 'Invalid Car')
        
    @bp.arguments(CarsSchema)
    def put(self, car_data, car_id):
        cars = CarsModel.query.get(car_id)
        if cars:
            cars.body = car_data['body']
            cars.commit()
        return {'message': "invalid"}, 400

    def delete(self, car_id):
        cars = CarsModel.query.get(car_id)
        if cars:
                cars.delete()
                del cars[car_id]
                return{ 'message': f'model Deleted'}, 202
                return {'Message': "Invalid"}, 400
            
@bp.route('/car')
class CarsList(MethodView):

    @bp.response(200, CarsSchema(many = True))
    def get(self):
        return CarsModel.query.all()
    

    @bp.arguments(CarsSchema)
    def post(self, car_data):
        try:
            cars = CarsModel
            cars.car_id = car_data['car_id']
            cars.body = car_data['body']
            cars.commit()
            return{ 'message' : f'{car_data["car"]} created'}, 201
        except:
            return {'message': 'Invalid Car'}, 401



@bp.response(200, CarsSchema(many=True))
@bp.get('/')
def car():
    return { 'cars': list(cars.values())}, 200


@bp.post('/')
@bp.arguments(CarsSchema)
def create_car(json_body):
    cars[uuid4()] = json_body
    return{ 'message' : f'{json_body["car"]} created'}, 201


# @bp.get('/car/<car_id>')
# @bp.response(200, CarsSchema)
# def get_car(car_id):
#      try:
#          return{'car': cars[car_id]}, 200
#      except:
#          return{'message': 'invalid car'}, 400


@bp.put('/<car_id>')
def update_car(car_id):
    try:
     car = cars[car_id]
     cars_data = request.get_json()
     if cars_data[car_id] != cars[car_id]:
            cars[car_id] = cars_data[car_id]
     return { 'message': f'{car["model"]} updated'}, 202
    except KeyError:
        return {'message': "invalid"}, 400



# @bp.delete('/<car_id>')
# def delete_user(car_id):
#     #cars_data = request.get_json()
#     #model = cars_data['model']
#     try:
#         del cars[car_id]
#         return{ 'message': f'model Deleted'}, 202
#     except:
#         return {'Message': "Invalid"}, 400