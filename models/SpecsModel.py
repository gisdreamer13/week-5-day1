from datetime import datetime

from app import db

class SpecsModel(db.Model):

    __tablename__ = 'specs'

    id = db.Column(db.Integer, primary_key = True)
    hp = db.Column(db.String, nullable = False)
    timestamp = db.Column(db.String)
    specs_id = db.Column(db.Integer, db.ForeignKey('specs.id'), nullable = False)

    def __repr__(self):
        return f'<post: {self.body}>'
    
    def commit(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    def from_dict(self, specs_dict):
        for k, v in specs_dict.items():
            if k != 'password':
                setattr(self, k, v)
            else:
                setattr(self, 'password_hash', generate_passsword_hash(v) )
                