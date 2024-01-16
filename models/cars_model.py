from datetime import datetime

from app import db

from werkzeug.security import generate_password_hash, check_password_hash

# followers = db.Table( 'followers',
#   db.Column('follower_id', db.Integer, db.ForeignKey('cars.id')),
#   db.Column('followed_id', db.Integer, db.ForeignKey('cars.id'))  
# )

class CarsModel(db.Model):

  __tablename__ = 'Cars'

  id = db.Column(db.Integer, primary_key = True)
  username = db.Column(db.String(50), nullable = False, unique = True)
  email = db.Column(db.String(75), nullable = False, unique = True)
  password_hash = db.Column(db.String(250), nullable = False )
  # first_name = db.Column(db.String(30))
  # last_name = db.Column(db.String(30))
  # followed = db.relationship('CarsModel',
  #                           secondary = 'followers',
  #                           primaryjoin = followers.c.follower_id == id,
  #                           secondaryjoin = followers.c.followed_id == id,
  #                           backref = db.backref('followers', lazy = 'dynamic')
  #                           )
  # cars = db.relationship('SpecsModel',back_populates ='cars', lazy='dynamic', cascade= 'all, delete')
  
  def __repr__(self):
    return f'<Cars: {self.username}>'

  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()

  def from_dict(self, cars_dict):
    for k, v in cars_dict.items():
      if k != 'password':
        setattr(self, k, v)
      else:
        setattr(self, 'password_hash', generate_password_hash(v))
        # self.password_hash = v

  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

  def is_following(self, cars):
    return cars in self.followed
  
  def follow(self, cars):
    if self.is_following(cars):
      return
    self.followed.append(cars)

  def unfollow(self,cars):
    if not self.is_following(cars):
      return
    self.followed.remove(cars)

class SpecsModel(db.Model):

  __tablename__ = 'specs'

  id = db.Column(db.Integer, primary_key = True)
  body = db.Column(db.String, nullable = False)
  timestamp = db.Column(db.DateTime, default = datetime.utcnow())
  # user_id = db.Column(db.Integer, db.ForeignKey('specs.id'), nullable = False)
  # user = db.relationship('CarsModel', back_populates = 'specs')

  def __repr__(self):
    return f'<Specs: {self.body}>'
  
  def commit(self):
    db.session.add(self)
    db.session.commit()

  def delete(self):
    db.session.delete(self)
    db.session.commit()