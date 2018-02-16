from datetime import datetime
from flask import (
    render_template,
    flash, redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import login, db
from app.rentals import rentals

@rentals.route('/new', methods=['GET', 'POST'])
def new():
    return render_template('rentals/new.html',
                           title='Rental')
