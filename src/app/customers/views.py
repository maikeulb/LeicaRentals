import sys
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
    customers = Customer.query.all()
    return render_template('customers/index.html',
                           customers=customers,
                           title='Customers')


@customers.route('/new', methods=['GET', 'POST'])
def new():
    membership_types = MembershipType.query \
            .all()
    form = CustomerForm()
    form.membership_type_id.choices = [(m.id, m.name) for m in membership_types]
    if form.validate_on_submit():
        customer = Customer()
        form.populate_obj(customer)
        try:
            db.session.add(customer)
            db.session.commit()
            flash('Customer added!', 'success')
            print('hi')
            return redirect(url_for('customers.index'))
        except:
            db.session.rollback()
            flash('Error adding customer.', 'danger')

    return render_template('customers/new.html',
                           form=form,
                           title='Customers')


@customers.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    customer = Customer.query \
            .filter_by(id=id) \
            .first_or_404()
    membership_types = MembershipType.query \
            .all()
    form = CustomerForm(obj=customer)
    form.membership_type_id.choices = [(m.id, m.name) for m in membership_types]
    if form.validate_on_submit():
        form.populate_obj(customer)
        try:
            form.populate_obj(customer)
            db.session.add(customer)
            db.session.commit()
            flash('Customer is updated!', 'success')
            return redirect(url_for('customers.index'))
        except:
            db.session.rollback()
            flash('Error editing customer.', 'danger')

    membership_types = MembershipType.query.all()
    return render_template('customers/edit.html',
                           membership_types=membership_types,
                           form=form,
                           title='Customers')


@customers.route('/details/<id>')
def details(id):
    customer = Customer.query \
            .filter_by(id=id) \
            .first_or_404()

    return render_template('customers/details.html',
                           customer=customer,
                           title='Customers')


@customers.route('/delete/<id>', methods=['POST'])
def delete(id):
    customer = Customer.query \
            .filter_by(id=id).first_or_404()
    try:
        db.session.delete(customer)
        db.session.commit()
        flash('Delete successfully.', 'success')
    except:
        db.session.rollback()
        flash('Error delete  customer.', 'danger')

    return redirect(url_for('customers.index'))
