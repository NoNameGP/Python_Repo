from ..app import db
from datetime import datetime
from sqlalchemy.orm import relationship

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)
    email = db.Column(db.String(255), nullable=True)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.dateTime, nullable=False, default=datetime.utcnow)
    marks = relationship('Mark', back_populates='user')

    def __repr__(self):
        return f"User {self.id}: {self.username}"
