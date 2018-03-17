import sys
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
from app.api.errors import bad_request
import json
from app.models import (
    Customer,
    Lens,
    Rental
)


@api.route('/rentals')
def get_rentals():
    rental_query = Rental.query
    rentals = rental_query.all()
    response = jsonify([rental.to_dict() for rental in rentals])
    return response


@api.route('/rentals/', methods=['POST'])
def create_rental():
    data = request.get_json() or {}
    customer = Customer.query.get_or_404(data["customerId"])
    lenses = []
    for id in data["lensIds"]:
        lenses.append(Lens.query.get_or_404(id))

    for lens in lenses:
        if lens.number_available == 0:
            return bad_request("lens is not available")

        lens.number_available -= 1
        rental = Rental()
        rental.customer = customer
        rental.lens = lens
        db.session.add(rental)

    db.session.commit()
    response = jsonify({"result": "success"})
    return response


@api.route('/rentals/<int:id>', methods=['DELETE'])
def delete_rental(id):
    rental = Rental.query.get_or_404(id)
    lens = rental.lens
    lens.number_available += 1

    db.session.delete(rental)
    db.session.commit()
    response = jsonify({'data': 'success'})
    return response
