import sys
from app.extensions import db
from datetime import datetime


class Customer(db.Model):
    __tablename__ = 'customers'

    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(140))
    last_name = db.Column(db.String(140))
    email = db.Column(db.String(140))
    is_signed_up = db.Column(db.Boolean, nullable=True)
    date_of_birth = db.Column(db.DateTime)
    membership_type_id = db.Column(
        db.Integer, db.ForeignKey('membership_types.id'))

    membership_type = db.relationship(
        'MembershipType'
    )

    @property
    def full_name(self):
        return '{0}, {1}'.format(self.last_name.title(),
                                 self.first_name.title())

    def from_dict(self, data):
        for field in ['first_name', 'last_name', 'email', 'date_of_birth',
                      'membership_type_id']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'full_name': self.full_name,
            'email': self.email,
            'date_of_birth': self.date_of_birth,
            'membership_type_id': self.membership_type_id,
            'membership_type_name': self.membership_type.name
        }
        return data
