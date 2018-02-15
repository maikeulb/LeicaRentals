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
    # membership_types = MembershipType.query.all()
    form = CustomerForm()
    # form.membership_type_id.choices = [(m.id, m.name) for m in membership_types]
    if form.validate_on_submit():
        # customer = Customer(first_name=form.first_name.data,
                            # last_name=form.last_name.data,
                            # date_of_birth=form.date_of_birth.data,
                            # membership_type_id=form.membership_type_id.data)
        customer = Customer()
        form.populate_obj(customer)
        try:
            db.session.add(customer)
            db.session.commit()
            flash('Customer is added!', 'success')
            return redirect(url_for('customers.index'))
        except:
            db.session.rollback()
            flash('Error adding customer.', 'danger')

    return render_template('customers/create.html',
                           form=form,
                           title='Customers')


@customers.route('/edit', methods=['GET', 'POST'])
def edit_customer(id):
    # membership_types = MembershipType.query.all()
    customer = Customer.query \
                        .join(Customer.membership_types) \
                        .filtery_by(id=id) \
                        .first_or_404()
    # form.membership_type_id.choices = [(m.id, m.name) for m in membership_types]
    form = CustomerForm(obj=customer)
    if form.validate_on_submit():
        form.populate_obj(customer)
        try:
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
def get_customer_details(id):

    customer = Customer.query \
                   .join(Customer.membership_types) \
                   .filtery_by(id=id) \
                   .first_or_404()

    return render_template('customers/details.html',
                           customer=customer,
                           title='Customers')

@customers.route('/delete/<id>', methods=('POST'))
def delete_customer(id):

    customer = Customer.query \
                   .filtery_by(id=id) \
                   .first_or_404()
    try:
        db.session.delete(customer)
        db.session.commit()
        flash('Delete successfully.', 'success')
    except:
        db.session.rollback()
        flash('Error delete  customer.', 'danger')

    return redirect(url_for('customers.index'))
