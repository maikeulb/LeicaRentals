from datetime import datetime
from flask import (
    render_template, 
    flash, redirect, 
    url_for, 
    request,
    current_app
)
from flask_login import current_user, login_required
from app.customers.forms import LensForm
from app.extensions import login, db
from app.customers import customers
from app.models import (
    Lens,
    Format,
)

@lens.route('/')
@lens.route('/index')
def index():
    lenses = Lens.query \
            .join(Lens.formats) \
            .all()
    return render_template('lens/index.html',
                           lenses=lenses,
                           title='Lenses')

@lens.route('/new', methods=['GET', 'POST'])
def new_lens(id):
    form = LensForm(obj=lens)
    if form.validate_on_submit():
        form.populate_obj(lens)
        try:
            db.session.add(lens)
            db.session.commit()
            flash('Lens is updated!', 'success')
            return redirect(url_for('lens.index'))
        except:
            db.session.rollback()
            flash('Error editing customer.', 'danger')

    formats = Format.query.all()
    return render_template('lens/create.html',
                           formats=formats,
                           form=form,
                           title='Lens')


@lens.route('/edit', methods=['GET', 'POST'])
def edit_lens(id):
    lens = Lens.query \
               .join(Customer.formats) \
               .filtery_by(id=id) \
               .first_or_404()
    form = LensForm(obj=lens)
    if form.validate_on_submit():
        form.populate_obj(lens)
        try:
            db.session.add(lens)
            db.session.commit()
            flash('Lens is updated!', 'success')
            return redirect(url_for('lens.index'))
        except:
            db.session.rollback()
            flash('Error editing customer.', 'danger')

    formats = Format.query.all()
    return render_template('lens/edit.html',
                           formats=formats,
                           form=form,
                           title='Lens')


@lens.route('/details/<id>')
def get_lens_details(id):
    lens = Lens.query \
           .join(Lens.formats) \
           .filtery_by(id=id) \
           .first_or_404()

    return render_template('lens/details.html',
                           lens=lens,
                           title='Lens')

@lens.route('/delete/<id>', methods=('POST'))
def delete_lens(id):

    lens = Lens.query \
               .filtery_by(id=id) \
               .first_or_404()
    try:
        db.session.delete(lens)
        db.session.commit()
        flash('Delete successfully.', 'success')
    except:
        db.session.rollback()
        flash('Error delete  customer.', 'danger')

    return redirect(url_for('lens.index'))
