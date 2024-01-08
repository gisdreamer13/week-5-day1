
from flask import request
from uuid import uuid4

from . import bp
from db import specs, cars





@bp.get('/specs')
def get_posts():
    return{'posts': list(specs.values())}

@bp.get('/specs/<spec_id>')
def get_specs(spec_id):
    try:
        return{'/specs': specs[spec_id]}, 200
    except:
        return {'Message': "Invalid"}, 400

@bp.post('/specs')
def create_post():
    specs_data = request.get_json()
    specs[uuid4()] = specs_data
    car_id = specs_data['car_id']
    if car_id in cars:
        cars[uuid4()] = specs_data
        return { 'message': "Car Added"}, 201
    return { 'message': "Invalid User"}, 401

@bp.put('/specs/<spec_id>')
def update_post(spec_id):
    try:
        specs = specs[spec_id]
        spec_data = request.get_json()
        if spec_data['spec_id'] == specs['spec_id']:
            specs['body'] = spec_data['body']
            return {'message': "specs updated"}, 202
        return {'message': "Unauthorized"}, 401
    except:
        return {'message': "invalid"}, 400

@bp.delete('/specs/<spec_id>')
def delte_post(spec_id):
    try:
        del specs[spec_id]
        return {'message': "specs deleted"}, 202
    except:
        return {'message': "Invalid post"}, 202