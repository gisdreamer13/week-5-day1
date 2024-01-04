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

@app.put('/car')
def update_car():
    return

@app.delete('/user')
def delete_user():
    pass

#post routes

@app.get('/post')
def get_posts():
    return

@app.post('/post')
def create_post():
    return

@app.put('/post')
def update_post():
    return

@app.delete('/post')
def delte_post():
    return