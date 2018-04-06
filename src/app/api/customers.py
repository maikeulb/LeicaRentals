from sqlalchemy import func
from flask import (
    request,
    jsonify,
)
from app.extensions import db
from app.api import api
from app.models import (
    Customer,
)


@api.route('/customers', defaults={'query': None})
def get_customers(query):
    query = request.args.get('query')
    customer_query = Customer.query

    if query:
        customer_query = \
            customer_query.filter(func.lower(Customer.first_name).contains(func.lower(query)) |
                                  func.lower(Customer.last_name).contains(func.lower(query)))

    customers = customer_query.all()
    response = jsonify([customer.to_dict() for customer in customers])
    return response


@api.route('/customers/<int:id>', methods=['DELETE'])
def delete_customer(id):
    Customer.query.filter_by(id=id).delete()
    db.session.commit()

    response = jsonify({'data': 'success'})
    return response
