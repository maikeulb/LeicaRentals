import sys
from flask import (
    render_template,
    flash, redirect,
    url_for,
    request,
)
from flask_login import login_required
from app.lenses.forms import LensForm
from app.extensions import db
from app.lenses import lenses
from app.models import (
    Lens,
    Mount,
    FocalLength,
)


@lenses.before_request
@login_required
def require_login():
    pass


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
    mounts = Mount.query \
        .all()
    focal_lengths = FocalLength.query \
        .all()
    form = LensForm()
    form.mount_id.choices = [(f.id, f.name) for f in mounts]
    form.focal_length_id.choices = [(f.id, f.name) for f in focal_lengths]
    if form.validate_on_submit():
        lens = Lens()
        form.populate_obj(lens)
        db.session.add(lens)
        db.session.commit()
        flash('Lens added!', 'success')
        return redirect(url_for('lenses.index'))

    return render_template('lenses/new.html',
                           form=form,
                           title='Lens')


@lenses.route('/edit/<id>', methods=['GET', 'POST'])
def edit(id):
    lens = Lens.query \
               .filter_by(id=id) \
               .first_or_404()
    mounts = Mount.query \
        .all()
    focal_lengths = FocalLength.query \
        .all()
    form = LensForm()
    form = LensForm(obj=lens)
    form.mount_id.choices = [(f.id, f.name) for f in mounts]
    form.focal_length_id.choices = [(f.id, f.name) for f in focal_lengths]
    if form.validate_on_submit():
        form.populate_obj(lens)
        db.session.add(lens)
        db.session.commit()
        flash('Lens updated!', 'success')
        return redirect(url_for('lenses.index'))

    return render_template('lenses/edit.html',
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
    db.session.delete(lens)
    db.session.commit()
    flash('Delete successfully.', 'success')

    return redirect(url_for('lenses.index'))
