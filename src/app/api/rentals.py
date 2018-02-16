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
import json
from app.models import (
    Customer,
)


@api.route('/api/rentals/', methods=['POST'])
def create_rental(id):
    data = request.get_json() or {}

    customer = Customer.query.get_or_404(data["customer_id")
    lens = Lens.query.get_or_404(data["lens_id")

    foreach lens in lenses:
        if lens.stock == 0:
            return badrequest("lens is not available")

        lens.stock = lens.stock - 1
        
        rental = Rental()
        rental.customer = customer
        rental.lens = lens
        db.session.add(lens)

    db.session.commit()
    response = jsonify({"result": "success"})

    return response
