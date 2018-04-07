import sys
from sqlalchemy import func
from flask import (
    request,
    jsonify,
)
from app.extensions import db
from app.api import api
from app.models import (
    Lens,
)


@api.route('/lenses', defaults={'query': None})
def get_lenses(query):
    # lens_query = Lens.query.filter(Lens.number_available > 0)
    query = request.args.get('query')
    lens_query = Lens.query.join(Lens.mount).join(Lens.focal_length)
    if query:
        lens_query = \
            lens_query.filter(func.lower(
                Lens.name).contains(func.lower(query)))
    lenses = lens_query.all()

    response = jsonify([lens.to_dict() for lens in lenses])
    return response


@api.route('/lenses/<int:id>', methods=['DELETE'])
def delete_lens(id):
    Lens.query.filter_by(id=id).delete()
    db.session.commit()

    response = jsonify({'data': 'success'})
    return response
