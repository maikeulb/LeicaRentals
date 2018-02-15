from app.extensions import db
from datetime import datetime


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    name  = db.Column(db.String(140))
    birth_date = db.Column(db.DateTime)
    is_subscribed = db.Column(db.Boolean)
    membership_type_id = db.Column(db.Integer, db.ForeignKey('membership_types.id'))

    membership_type = db.relationship(
        'MembershipType',
        backref='customer',
        lazy='dynamic'
    )
