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
from app.lenses.forms import LensForm
from app.extensions import login, db
from app.lenses import lenses
from app.models import (
    Lens,
    Format,
)


@lenses.route('/')
@lenses.route('/index')
def index():
    lenses = Lens.query \
            .all()

    return render_template('lenses/index.html',
                           lenses=lenses,
                           title='Lenses')

@lenses.route('/new', methods=['GET', 'POST'])
def new():
    formats = Format.query \
            .all()
    form = LensForm()
    form.format_id.choices = [(f.id, f.name) for f in formats]
    if form.validate_on_submit():
        lens = Lens()
        form.populate_obj(lens)
        try:
            db.session.add(lens)
            db.session.commit()
            flash('Lens added!', 'success')
            return redirect(url_for('lenses.index'))
        except:
            db.session.rollback()
            flash('Error editing lens.', 'danger')

    formats = Format.query.all()
    return render_template('lenses/new.html',
                           form=form,
                           title='Lens')


@lenses.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    lens = Lens.query \
               .filter_by(id=id) \
               .first_or_404()
    formats = Format.query.all()
    form = LensForm(obj=lens)
    form.format_id.choices = [(f.id, f.name) for f in formats]
    if form.validate_on_submit():
        try:
            form.populate_obj(lens)
            db.session.add(lens)
            db.session.commit()
            flash('Lens is updated!', 'success')
            return redirect(url_for('lenses.index'))
        except:
            db.session.rollback()
            flash('Error editing customer.', 'danger')

    formats = Format.query.all()
    return render_template('lenses/edit.html',
                           formats=formats,
                           form=form,
                           title='Lens')


@lenses.route('/details/<id>')
def details(id):
    lens = Lens.query \
            .filter_by(id=id) \
            .first_or_404()

    return render_template('lenses/details.html',
                           lens=lens,
                           title='Lens')

@lenses.route('/delete/<id>', methods=['POST'])
def delete(id):
    lens = Lens.query \
               .filter_by(id=id) \
               .first_or_404()
    try:
        db.session.delete(lens)
        db.session.commit()
        flash('Delete successfully.', 'success')
    except:
        db.session.rollback()
        flash('Error delete  customer.', 'danger')

    return redirect(url_for('lenses.index'))
