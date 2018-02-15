from app.extensions import db
from datetime import datetime


class Format(db.Model):
    __tablename__ = 'formats'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
