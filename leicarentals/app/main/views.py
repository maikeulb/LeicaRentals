from flask import (
    render_template,
)
from app.main import main


@main.route('/')
@main.route('/index')
def index():
    return render_template('main/index.html',
                           title='Home')
