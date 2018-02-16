from app.extensions import db
from datetime import datetime


class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    date_rented = db.Column(db.DateTime)
    date_returned = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    lens_id = db.Column(db.Integer, db.ForeignKey('lenses.id'))

    customer = db.relationship('Customer')
    lens = db.relationship('Lens')

