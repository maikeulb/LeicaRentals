from app.extensions import db
from datetime import datetime


class MembershipType(db.Model):
    __tablename__ = 'membership_types'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    sign_up_fee = db.Column(db.Integer)
    duration_in_months = db.Column(db.Integer)
    discount_rate = db.Column(db.Integer)
