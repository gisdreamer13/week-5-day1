from flask import Flask, request
from uuid import uuid4

app = Flask(__name__)

cars = {
    'nissan' : {
        'model' : 'skyline',
        'year' : '1998'
    },
    'honda' : {
        'model' : 'type R',
        'year' : '1997'
    },
    'subaru' : {
        'model' : 'STI',
        'year' : '2020'
    },
    'mitsubishi' : {
        'model' : 'evo',
        'year' : '2015'
    }
}

specs = {
    'nissan' : {
        'HP' : '276',
        'car_id': 'nissan'
    },
    'honda' : {
        'HP' : '182',
        'car_id' : 'honda'
    },
    'subaru' : {
        'HP' : '310',
        'car_id' : 'subaru'
    },
    'mitsubishi' : {
        'HP' : '303',
        'car_id' : 'mitsubishi'
    }
}


@app.get('/car')
def car():
    return { 'cars': list(cars.values())}, 200


@app.post('/car')
def create_car():
    json_body = request.get_json()
    cars[uuid4()] = json_body
    return{ 'message' : f'{json_body["car"]} created'}, 201

@app.put('/car/<car_id>')
def update_car(car_id):
    try:
     car = cars[car_id]
     cars_data = request.get_json()
     car|= cars_data
     return { 'message': f'{car["model"]} updated'}, 202
    except KeyError:
        return {'message': "invalid"}, 400

@app.delete('/car/<car_id>')
def delete_user(car_id):
    #cars_data = request.get_json()
    #model = cars_data['model']
    try:
        del cars[id]
        return{ 'message': f'model Deleted'}, 202
    except:
        return {'Message': "Invalid"}, 400
    

#post routes

@app.get('/specs')
def get_posts():
    return{'posts': list(specs.values())}

@app.post('/specs')
def create_post():
    specs_data = request.get_json()
    specs[uuid4()] = specs_data
    car_id = specs_data['car_id']
    if car_id in cars:
        cars[uuid4()] = specs_data
        return { 'message': "Car Added"}, 201
    return { 'message': "Invalid User"}, 401

@app.put('/specs')
def update_post():
    return

@app.delete('/specs')
def delte_post():
    return