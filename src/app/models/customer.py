from app.extensions import db
from datetime import datetime


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140))
    last_name = db.Column(db.String(140))
    date_of_birth = db.Column(db.DateTime)
    is_subscribed = db.Column(db.Boolean)
    membership_type_id = db.Column(db.Integer, db.ForeignKey('membership_types.id'))

    membership_types = db.relationship(
        'MembershipType',
        backref='customer',
        lazy='dynamic'
    )
