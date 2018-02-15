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
)

@customers.route('/')
@customers.route('/index')
def index():
    customers = Customer.query.all()
    return render_template('customers/index.html',
                           customers=customers,
                           title='Customers')

@customers.route('/new')
def new_customer():
    form = CustomerForm()
    membership_types = MembershipType.query.all()
    if form.validate_on_submit():
    customer = Customer(name=form.body.data,
                        birth_date=form.body.birth_date,
                        membership_type_id=form.body.membership_type_id)

    return render_template('customers/create.html',
                           membership_types=membership_types,
                           form=form,
                           title='Customers')

@customers.route('/new/:id')
def new_customer(id):
    customers = Customer.query.findById(id)
    membership_types = MembershipType.query.all()
    if form.validate_on_submit():
    customer = Customer(name=form.body.data,
                        birth_date=form.body.birth_date,
                        membership_type_id=form.body.membership_type_id)

    return render_template('customers/edit.html',
                           membership_types=membership_types,
                           form=form,
                           title='Customers')
