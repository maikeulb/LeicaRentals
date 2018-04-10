from flask import (
    render_template,
    redirect,
    request,
)
from flask_login import login_required
from app.rentals import rentals
from app.models import (
    Rental,
)


@rentals.before_request
@login_required
def require_login():
    pass


@rentals.route('/')
@rentals.route('/index')
def index():
    rentals = Rental.query \
        .all()

    return render_template('rentals/index.html',
                           rentals=rentals,
                           title='Rental')


@rentals.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('rentals/new.html',
                           title='Rental')
