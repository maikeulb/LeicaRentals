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
)

@api.route('/customers/<query>', defaults={'query': None})
def get_customers(query):
    customer_query = Customer.query

    if query:
        customer_query = customer_query.filter(Customer.last_name.contains(query))
    customers = customer_query.all()

    response = jsonify([customer.to_dict() for customer in customers])
    return response


@api.route('/customers/<int:id>')
def get_customer(id):
    customer = Customer.query.get_or_404(id)

    response = jsonify(customer.to_dict())
    return response


@api.route('/customers/', methods=['POST'])
def create_customer():
    data = request.get_json() or {}
    # if 'first_name' not in data or 'last_name' not in data \
       # return bad_request('must include first_name, last_name')

    customer = Customer()
    customer.from_dict(data)

    db.session.add(customer)
    db.session.commit()

    response = jsonify(customer.to_dict())
    return response


@api.route('/customers/<int:id>', methods=['PUT'])
def update_customer(id):
    customer = Customer.query.filter_by(id=id).first_or_404()
    customer.from_dict(request.get_json() or {})

    db.session.commit()

    response = jsonify(customer.to_dict())
    return response


@api.route('/customers/<int:id>', methods=['Delete'])
def delete_customer(id):
    Customer.query.filter_by(id=id).delete()
    db.session.commit()

    response = jsonify({'data': 'success'})
    return response
