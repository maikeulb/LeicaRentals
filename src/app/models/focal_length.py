from app.extensions import db


class FocalLength(db.Model):
    __tablename__ = 'focal_lengths'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
