from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship
from flask_login import UserMixin
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()


class BaseModel:
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)


class Coordinate:
    X = db.Column(db.Float)
    Y = db.Column(db.Float)


class User(db.Model, BaseModel, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    marks = relationship('Mark', back_populates='markOwner')
    routes = relationship('Route', back_populates='routeOwner')

    def __init__(self, email, password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User {self.id}: {self.email}"

    def set_password(self, password):
        self.password = bcrypt.generate_password_hash(password).decode('utf-8')

    def check_password(self, password):
        return bcrypt.check_password_hash(self.password, password)

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    @staticmethod
    def find_user(email):
        return User.query.filter_by(email=email).first()


class Mark(db.Model, BaseModel, Coordinate):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    markOwner = relationship('User', back_populates='marks')
    name = db.Column(db.String(255), nullable=False)

    def __init__(self, user, name, point):
        self.userId = user.id
        self.name = name
        self.X = point['X']
        self.Y = point['Y']

    def __repr__(self):
        return f"Mark {self.name}: {self.endX}"


class Object(db.Model, BaseModel, Coordinate):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    objectOwner = relationship('Route', back_populates='objects')

    def __init__(self, route, X, Y):
        self.route = route.id
        self.X = X
        self.Y = Y

    def __repr__(self):
        return f"Object {self.route}: {self.pointX},{self.pointY}"


class PassPoint(db.Model, BaseModel, Coordinate):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    passPointOwner = relationship('Route', back_populates='passPoints')

    def __init__(self, route, X, Y):
        self.route = route.id
        self.X = X
        self.Y = Y

    def __repr__(self):
        return f"PassPoint {self.route}: {self.pointX},{self.pointY}"


class Route(db.Model, BaseModel):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    routeOwner = relationship('User', back_populates='routes')

    startX = db.Column(db.Float)
    startY = db.Column(db.Float)
    endX = db.Column(db.Float)
    endY = db.Column(db.Float)

    objects = relationship('Object', back_populates='objectOwner')
    passPoints = relationship('PassPoint', back_populates='passPointOwner')

    def __init__(self, user, start_point, end_point):
        self.user = user.id
        self.startX = start_point['X']
        self.startY = start_point['Y']
        self.endX = end_point['X']
        self.endY = end_point['Y']

    def __repr__(self):
        return f"Route: {self.user.id},{self.id}"