from marshmallow import Schema, fields

class CarsSchema(Schema):
    id = fields.Str(dump_only = True)
    model = fields.Str(required = True)
    year = fields.Str(required = True)
    password = fields.Str(required = True, load_only = True)


class SpecsSchema(Schema):
    HP = fields.Str(dump_only = True)
    car_id = fields.Str(required = True)
    timestamp = fields.DateTime(dump_only = True)

    specs_id = fields.Str(required = True)