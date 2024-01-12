from app import db

from werkzeug.security import generate_password_hash, check_password_hash

class CarsModel(db.Model):

    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key = True)
    model = db.Column(db.String(50), nullable = False, unique = True)
    year = db.Column(db.String(50), nullable = False, unique = True)
    password_hash = db.Column(db.String(30), nullable = False)

def __repr__(self):
    return f'<Cars: {self.username}>'

def commit(self):
    db.session.add(self)
    db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()