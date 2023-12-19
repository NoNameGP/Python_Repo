from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///viewMe.db'  # SQLite 데이터베이스
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

api = Api(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from datetime import datetime
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    #marks = relationship('Mark', back_populates='user')

    def __init__(self,username,password):
        self.username = username
        self.password = password

    def __repr__(self):
        return f"User {self.id}: {self.username}"


user = User("name","pw")

if __name__ == '__main__':
    app.run(debug=True)