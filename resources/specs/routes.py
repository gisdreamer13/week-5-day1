from flask import request
from flask_jwt_extended import jwt_required, get_jwt_identity
from uuid import uuid4
from flask.views import MethodView
from flask_smorest import abort

from models import SpecsModel
from schemas import SpecsSchema, SpecsSchemaNested

from . import bp
# post routes

@bp.route('/<specs_id>')
class Specs(MethodView):

  @bp.response(200, SpecsSchemaNested)
  def get(self, specs_id):
    specs = SpecsModel.query.get(specs_id)
    if specs:
      return specs 
    abort(400, message='Invalid Specs')

  # @jwt_required
  @bp.arguments(SpecsSchema)
  def put(self, specs_data, specs_id):
    specs = SpecsModel.query.get(specs_id)
    if specs:
      specs.body = specs_data['body']
      specs.commit()   
      return {'message': 'specs updated'}, 201
    return {'message': "Invalid Spec Id"}, 400
    
  # @jwt_required()
  def delete(self, specs_id):
    specs = SpecsModel.query.get(specs_id)
    if specs:
      specs.delete()
      return {"message": "Post Deleted"}, 202
    return {'message':"Invalid Post or User"}, 400

@bp.route('/')
class SpecsList(MethodView):

  @bp.response(200, SpecsSchema(many = True))
  def get(self):
    return SpecsModel.query.all()
  
  # @jwt_required()
  @bp.arguments(SpecsSchema)
  def post(self, specs_data):
    try:
      specs = SpecsModel()
      # specs.specs_id = get_jwt_identity() 
      specs.HP = specs_data['HP']
      specs.car_id = specs_data['car_id']
      specs.commit()
      return { 'message': "Specs Created" }, 201
    except:
      return { 'message': "Invalid Specs"}, 401