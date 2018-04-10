from app.extensions import db


class Mount(db.Model):
    __tablename__ = 'mounts'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(140))
