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
    mount_id = db.Column(db.Integer, db.ForeignKey('mounts.id'))
    focal_length_id = db.Column(db.Integer, db.ForeignKey('focal_lengths.id'))

    mount = db.relationship(
        'Mount',
        backref='mount'
    )

    focal_length = db.relationship(
        'FocalLength',
        backref='focal_length'
    )


    @property
    def lens_name(self):
        return '{0} {1}, {2}'.format(self.focal_length.name, self.name.title(),
                                 self.mount.name)

    def from_dict(self, data):
        for field in ['name','focal_length_id', 'date_added', 'release_date', 'number_in_stock',
                      'number_available', 'mount_id', 'lens_name']:
            if field in data:
                setattr(self, field, data[field])

    def to_dict(self):
        data = {
            'id': self.id,
            'name': self.name,
            'lens_name': self.lens_name,
            'date_added': self.date_added,
            'release_date': self.release_date,
            'number_in_stock': self.number_in_stock,
            'number_available': self.number_available,
            'focal_length_id': self.focal_length_id,
            'focal_length_name': self.focal_length.name,
            'mount_id': self.mount_id,
            'mount_name': self.mount.name
        }
        return data


