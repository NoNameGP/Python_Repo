from ..app import db
from datetime import datetime


class Object(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.Integer, nullable=False)
    y = db.Column(db.Integer, nullable=False)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.dateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"장애물 {self.id} : {self.x} , {self.y}"
