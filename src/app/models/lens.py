from app.extensions import db
from datetime import datetime


class Lens(db.Model):
    __tablename__ = 'lenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    date_added = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    release_date = db.Column(db.DateTime, index=True)
    stock = db.Column(db.Integer)
    format_id = db.Column(db.Integer, db.ForeignKey('formats.id'))

    formats = db.relationship(
        'Format',
        backref='lens',
        lazy='dynamic'
    )
