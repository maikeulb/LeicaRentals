from datetime import datetime
from flask import (
    render_template,
    flash, redirect,
    url_for,
    request,
    current_app
)
from flask_login import current_user, login_required
from app.rentals.forms import RentalForm
from app.extensions import login, db
from app.rentals import rentals

@rentals.route('/new', methods=['GET', 'POST'])
def new():
    form = RentalForm()
    if form.validate_on_submit():
        try:
            db.session.add(lens)
            db.session.commit()
            flash('Rental is a success!', 'success')
            return redirect(url_for('home.index'))
        except:
            db.session.rollback()
            flash('Error editing customer.', 'danger')

    return render_template('rentals/new.html',
                           form=form,
                           title='Lens')
