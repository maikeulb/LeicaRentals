from app.extensions import db
from datetime import datetime, date


class Rental(db.Model):
    __tablename__ = 'rentals'

    id = db.Column(db.Integer, primary_key=True)
    date_rented = db.Column(db.DateTime, default=datetime.utcnow)
    date_returned = db.Column(db.DateTime)
    customer_id = db.Column(db.Integer, db.ForeignKey('customers.id'))
    lens_id = db.Column(db.Integer, db.ForeignKey('lenses.id'))

    customer = db.relationship('Customer')
    lens = db.relationship('Lens')

    def from_dict(self, data):
        for field in ['date_rented', 'date_returned', 'customer_id',
                      'lens_id']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'date_rented': self.date_rented.strftime('%Y-%m-%d'),
            'customer_name': self.customer.full_name,
            'lens_name': self.lens.lens_name
        }
        return data


