from flask import request
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from . import bp
from db import specs

from schemas import SpecsSchema
from models.SpecsModel import SpecsModel
# user routes

@bp.route('/specs/<specs_id>')
class specs(MethodView):

  @bp.response(200, SpecsSchema)
  def get(self,specs_id):
    specs = SpecsModel.query.get(specs_id)
    if specs:
      return specs
    else:
      abort(400, message='Specs not found')
  

  @bp.arguments(SpecsSchema)
  def put(self, specs_data, specs_id):
      specs = SpecsModel.query.get(specs_id)
      if specs:
        specs.from_dict(specs_data)
        specs.commit()
        return { 'message': f'{specs["username"]} updated'}, 202
      abort(400, message = "Invalid User")

  def delete(self, specs_id):
    specs = SpecsModel.query.get(specs_id)
    if specs:
      specs.delete()
      return { 'message': f'User: {specs.username} Deleted' }, 202
    return {'message': "Invalid username"}, 400

@bp.route('/specs')
class specsList(MethodView):

  @bp.response(200, SpecsSchema(many = True))
  def get(self):
   return SpecsModel.query.all()

  @bp.arguments(SpecsSchema)
  def post(self, specs_data):
    try:
      specs = SpecsModel()
      specs.from_dict(specs_data)
      specs.commit()
      return { 'message' : f'{specs_data["username"]} created' }, 201
    except:
      abort(400, 'Specs already exsist')















# from flask import request
# from uuid import uuid4
# from flask.views import MethodView

# from schemas import SpecsSchema
# from . import bp
# from db import specs, cars


# @bp.route('/<specs_id>')
# class specs(MethodView):
#     @bp.response(200, SpecsSchema)
#     def get(self, specs_id):
#         try:
#             return specs[specs_id]
#         except:
#             return {'Message': "Invalid"}, 400

#     @bp.arguments(SpecsSchema)
#     def put(self, specs_data, specs_id):
#         try:
#             specs = specs[specs_id]
#             specs |= specs_data
#             return { 'message': f'{specs["specs"]} updated'}, 202
#         except KeyError:
#             return {'message': "Invalid User"}, 400

#     def delete(self, specs_id):
#          try:
#             del specs[specs_id]
#             return {'message': "specs deleted"}, 202
#          except:
#             return {'message': "Invalid post"}, 202


# @bp.route('/')
# class SpecList(MethodView):
    
#     @bp.response(200, SpecsSchema)
#     def get(self):
#         return{'posts': list(specs.values())}

#     @bp.arguments(SpecsSchema)
#     def post(self, specs_data):
#         specs_data = request.get_json()
#         specs[uuid4()] = specs_data
#         car_id = specs_data['car_id']
#         if car_id in cars:
#             cars[uuid4()] = specs_data
#             return { 'message': "Car Added"}, 201
#         return { 'message': "Invalid User"}, 401











# @bp.get('/specs')
# def get_posts():
#     return{'posts': list(specs.values())}

# @bp.get('/specs/<spec_id>')
# def get_specs(spec_id):
#     try:
#         return{'/specs': specs[spec_id]}, 200
#     except:
#         return {'Message': "Invalid"}, 400

# @bp.post('/specs')
# def create_post():
#     specs_data = request.get_json()
#     specs[uuid4()] = specs_data
#     specs_id = specs_data['car_id']
#     if specs_id in specs:
#         specs[uuid4()] = specs_data
#         return { 'message': "Car Added"}, 201
#     return { 'message': "Invalid User"}, 401

# @bp.put('/specs/<spec_id>')
# def update_post(spec_id):
#     try:
#         specs = specs[spec_id]
#         spec_data = request.get_json()
#         if spec_data['spec_id'] == specs['spec_id']:
#             specs['body'] = spec_data['body']
#             return {'message': "specs updated"}, 202
#         return {'message': "Unauthorized"}, 401
#     except:
#         return {'message': "invalid"}, 400

# @bp.delete('/specs/<spec_id>')
# def delte_post(spec_id):
#     try:
#         del specs[spec_id]
#         return {'message': "specs deleted"}, 202
#     except:
#         return {'message': "Invalid post"}, 202