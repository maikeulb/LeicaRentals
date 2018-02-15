from datetime import datetime
from flask import (
    render_template, 
    flash, redirect, 
    url_for, 
    request,
    current_app
)
from flask_login import current_user, login_required
from app.customers.forms import CustomerForm
from app.extensions import login, db
from app.customers import customers
from app.models import (
    Customer,
    MembershipType,
)


@customers.route('/')
@customers.route('/index')
def index():
    customers = Customer.query \
            .join(Customer.membership_types) \
            .all()
    return render_template('customers/index.html',
                           customers=customers,
                           title='Customers')


@customers.route('/new', methods=['GET', 'POST'])
def new_customer():

    form = CustomerForm()
    if form.validate_on_submit():
        customer = Customer(first_name=form.first_name.data,
                            last_name=form.last_name.data,
                            date_of_birth=form.date_of_birth.data,
                            membership_type_id=form.membership_type_id.data)
        db.session.add(customer)
        db.session.commit()
        flash('Customer is added!')
        return redirect(url_for('customers.index'))

    membership_types = MembershipType.query.all()
    return render_template('customers/create.html',
                           membership_types=membership_types,
                           form=form,
                           title='Customers')


@customers.route('/details/<id>')
def get_customer_details(id):
    customer = Customer.query \
                        .join(Customer.membership_types) \
                        .filtery_by(id=id) \
                        .first_or_404()

    return render_template('customers/details.html',
                           customer=customer,
                           title='Customers')
