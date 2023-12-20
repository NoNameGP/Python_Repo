from ..app import db
from datetime import datetime
from sqlalchemy.orm import relationship


class Mark(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    userId = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = relationship('User', back_populates='marks')
    name = db.Column(db.String(255), nullable=True)
    endPoint = db.Column(db.Long)
    status = db.Column(db.String(255), nullable=False, server_default='Active')
    createAt = db.Column(db.dateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f"Mark {self.name}: {self.endPoint}"
