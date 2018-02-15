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

@main.route('/', methods=['GET', 'POST'])
@main.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('rentals/index.html',
                           title='Home')
