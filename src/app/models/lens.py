from app.extensions import db
from datetime import datetime


class Lens(db.Model):
    __tablename__ = 'lenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    date_added = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    release_date = db.Column(db.DateTime, index=True)
    number_in_stock = db.Column(db.Integer)
    number_available = db.Column(db.Integer)
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))

    format = db.relationship('Format')

    def from_dict(self, data):
        for field in ['name', 'date_added', 'release_date',
                      'number_in_stock', 'number_available', 'format_id']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'date_added': self.date_added,
            'release_date': self.release_date,
            'number_in_stock': self.number_in_stock,
            'number_available': self.number_available,
            'format_id': self.format_id
        }
        return data


