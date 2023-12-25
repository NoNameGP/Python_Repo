from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from .conf import config

from datetime import datetime
from sqlalchemy.orm import relationship

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = config['db']  # SQLite 데이터베이스
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

with app.app_context():
    db.create_all()


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)
    marks = relationship('Mark', back_populates='User')

    def __init__(self, username, password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User {self.id}: {self.username}"


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='Marks')
    name = db.Column(db.String(255), nullable=True)
    endPoint = db.Column(db.Float)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Mark {self.name}: {self.endPoint}"



class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime(), nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"장애물 {self.id} : {self.x} , {self.y}"


if __name__ == '__main__':
    app.run(debug=True)
