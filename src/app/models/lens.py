from app.extensions import db
from datetime import datetime


class Lens(db.Model):
    __tablename__ = 'lenses'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
    date_added = db.Column(db.DateTime, index=True, default=datetime.utcnow)
    release_date = db.Column(db.DateTime, index=True)
    number_in_stock = db.Column(db.Integer)
    genre_id = db.Column(db.Integer, db.ForeignKey('genres.id'))

    genre = db.relationship(
        'Genre',
        backref='lens',
        lazy='dynamic'
    )
