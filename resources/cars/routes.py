from flask import request
from uuid import uuid4


from db import specs, cars
from . import bp





@bp.get('/')
def car():
    return { 'cars': list(cars.values())}, 200

@bp.get('/car/<car_id>')
def get_car(car_id):
    try:
        return{'car': cars[car_id]}, 200
    except:
        return{'message': 'invalid car'}, 400
    


@bp.post('/')
def create_car():
    json_body = request.get_json()
    for k in ['model', 'year', 'password']:
        if k not in json_body:
            return {'message': 'please include model year and password'}, 400
    cars[uuid4()] = json_body
    return{ 'message' : f'{json_body["car"]} created'}, 201

@bp.put('/<car_id>')
def update_car(car_id):
    try:
     car = cars[car_id]
     print(1)
     cars_data = request.get_json()
     print(2)
     if cars_data[car_id] != cars[car_id]:
            print(3)
            cars[car_id] = cars_data[car_id]
            print(4)
     return { 'message': f'{car["model"]} updated'}, 202
    except KeyError:
        return {'message': "invalid"}, 400

@bp.delete('/<car_id>')
def delete_user(car_id):
    #cars_data = request.get_json()
    #model = cars_data['model']
    try:
        del cars[car_id]
        return{ 'message': f'model Deleted'}, 202
    except:
        return {'Message': "Invalid"}, 400