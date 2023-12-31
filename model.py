from database import db
from datetime import datetime
from sqlalchemy.orm import relationship


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    marks = relationship('Mark', back_populates='user')

    def __init__(self,email):
        self.email = email

    def __repr__(self):
        return f"User {self.id}: {self.username}"


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='marks')
    name = db.Column(db.String(255), nullable=True)
    endPoint = db.Column(db.Float)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Mark {self.name}: {self.endPoint}"
