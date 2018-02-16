from app.extensions import db
from datetime import datetime


class Lens(db.Model):
    __tablename__ = 'rental'

    id = db.Column(db.Integer, primary_key=True)
    date_rented = db.Column(db.DateTime)
    date_returned = db.Column(db.DateTime)

    customer = db.relationship('Customer')
    lens = db.relationship('Lens')
