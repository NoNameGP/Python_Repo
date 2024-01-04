from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy.orm import relationship

db = SQLAlchemy()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)
    password = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    marks = relationship('Mark', back_populates='markOwner')
    routes = relationship('Route', back_populates='routeOwner')

    def __init__(self, email,password):
        self.email = email
        self.password = password

    def __repr__(self):
        return f"User {self.id}: {self.username}"


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    markOwner = relationship('User', back_populates='marks')
    name = db.Column(db.String(255), nullable=False)
    endX = db.Column(db.Float)
    endY = db.Column(db.Float)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Mark {self.name}: {self.endX}"
class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    objectOwner = relationship('Route', back_populates='objects')

    pointX = db.Column(db.Float)
    pointY = db.Column(db.Float)

    def __repr__(self):
        return f"Object {self.route}: {self.pointX},{self.pointY}"


class PassPoint(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    route = db.Column(db.Integer, db.ForeignKey('route.id'), nullable=False)
    passPointOwner = relationship('Route', back_populates='passPoints')

    pointX = db.Column(db.Float)
    pointY = db.Column(db.Float)

    def __repr__(self):
        return f"PassPoint {self.route}: {self.pointX},{self.pointY}"


class Route(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    routeOwner = relationship('User', back_populates='routes')

    startX = db.Column(db.Float)
    startY = db.Column(db.Float)
    endX = db.Column(db.Float)
    endY = db.Column(db.Float)

    objects = relationship('Object', back_populates='objectOwner')
    passPoints = relationship('PassPoint', back_populates='passPointOwner')

    def __repr__(self):
        return f"Route {self.user.id}: {self.startX},{self.startY}"
