from datetime import datetime
from flask import (
    render_template, 
    flash, redirect, 
    url_for, 
    request,
    current_app
)
from flask_login import current_user, login_required
from app.customers.forms import RentalsForm
from app.extensions import login, db
from app.customers import customers
from app.models import (
    Lens,
    Format,
)

@rentals.route('/')
@rentals.route('/index')
def index():
    lenses = Lens.query \
            .join(Lens.formats) \
            .all()
    return render_template('rentals/index.html',
                           lenses=lenses,
                           title='Lenses')

@rentals.route('/new', methods=['GET', 'POST'])
def new_lens():
    form = RentalsForm()
    if form.validate_on_submit():
        lens = Rental(name=form.name.data,
                        release_date=form.release_date.data,
                        format_id=form.format_id.data,
                        stock=form.stock.data)
        db.session.add(lens)
        db.session.commit()
        flash('Lens is added!')
        return redirect(url_for('lens.index'))

    formats = Format.query.all()
    return render_template('rentals/create.html',
                           formats=formats,
                           form=form,
                           title='Lens')

@rentals.route('/details/<id>')
def get_lens_details(id):
    lens = Lens.query \
           .join(Lens.formats) \
           .filtery_by(id=id) \
           .first_or_404()

    return render_template('rentals/edit.html',
                           lens=lens,
                           title='Lens')
