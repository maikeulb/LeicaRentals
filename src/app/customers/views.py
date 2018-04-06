import sys
from flask import (
    render_template,
    flash, redirect,
    url_for,
)
from flask_login import login_required
from app.customers.forms import CustomerForm
from app.extensions import db
from app.customers import customers
from app.models import (
    Customer,
    MembershipType,
)
from app.tasks import send_newsletter


@customers.before_request
@login_required
def require_login():
    pass


@customers.route('/')
@customers.route('/index')
@login_required
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
    form.membership_type_id.choices = [
        (m.id, m.name) for m in membership_types]
    if form.validate_on_submit():
        customer = Customer()
        form.populate_obj(customer)
        db.session.add(customer)
        db.session.commit()
        flash('Customer added!', 'success')
        return redirect(url_for('customers.index'))

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
    form.membership_type_id.choices = [
        (m.id, m.name) for m in membership_types]
    if form.validate_on_submit():
        form.populate_obj(customer)
        db.session.add(customer)
        db.session.commit()
        flash('Customer is updated!', 'success')
        return redirect(url_for('customers.index'))

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
    db.session.delete(customer)
    db.session.commit()
    flash('Delete successfully.', 'success')

    return redirect(url_for('customers.index'))


@customers.route('/newsletter')
def newsletter():
    customers = \
        Customer.query.filter_by(is_signed_up=True).all()
    emails = [c.email for c in customers]
    names = [c.first_name for c in customers]
    for i in range(0, len(emails)):
        body = render_template(
            'email/newsletter.html', name=names[i])
        send_newsletter('LeicaRentals NewsLetter',
                        [emails[i]],
                        body)

    flash('Sending newsletters')

    return redirect(url_for('customers.index'))
