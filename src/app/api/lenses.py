import sys
from sqlalchemy import func
from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.api import api
import json
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
        lens_query.filter(func.lower(Lens.name).contains(func.lower(query)))

    lenses = lens_query.all()
    response = jsonify([lens.to_dict() for lens in lenses])
    return response


@api.route('/lenses/<int:id>')
def get_lens(id):
    lens = Lens.query.get_or_404(id)

    response = jsonify(lens.to_dict())
    return response


@api.route('/lenses/', methods=['POST'])
def create_lens():
    data = request.get_json() or {}

    lens = Lens()
    lens.from_dict(data)

    db.session.add(lens)
    db.session.commit()

    response = jsonify(lens.to_dict())
    return response


@api.route('/lenses/<int:id>', methods=['PUT'])
def update_lens(id):
    lens = Lens.query.filter_by(id=id).first_or_404()
    lens.from_dict(request.get_json() or {})

    db.session.commit()

    response = jsonify(lens.to_dict())
    return response


@api.route('/lenses/<int:id>', methods=['DELETE'])
def delete_lens(id):
    Lens.query.filter_by(id=id).delete()
    db.session.commit()

    response = jsonify({'data': 'success'})
    return response
