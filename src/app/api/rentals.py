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
# from app.api.errors import bad_request
import json
from app.models import (
    Customer,
    Lens,
    Rental,
)


@api.route('/rentals/', methods=['POST'])
def create_rental():
    data = request.get_json() or {}
    customer = Customer.query.get_or_404(data["customerId"])
    print('**********************')
    lenses = []
    for id in data["lensIds"]:
        lenses.append(Lens.query.get_or_404(id))

    print(lenses,sys.stdout)
    for lens in lenses:
        # if lens.number_available == 0:
            # return bad_request("lens is not available")

        # lens.number_available -= 1
        rental = Rental()
        rental.customer = customer
        rental.lens = lens
        db.session.add(rental)

    db.session.commit()
    response = jsonify({"result": "success"})
    return response
