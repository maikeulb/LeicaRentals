import config
import os

from flask import (
    Flask,
    render_template,
    request,
    current_app
)
from app.extensions import bcrypt, csrf_protect, db, \
    login, migrate, moment, mail
from app.api import api as api_bp
from app.account import account as account_bp
from app.main import main as main_bp
from app.rentals import rentals as rentals_bp
from app.customers import customers as customers_bp
from app.lenses import lenses as lenses_bp
from app.newsletter import newsletter as newsletter_bp
from celery import Celery

celery = Celery(__name__,
                backend=os.environ.get('CELERY_RESULT_BACKEND'),
                broker=os.environ.get('CELERY_BROKER_URL'))


def create_app(config_class):
    app = Flask(__name__)
    app.config.from_object(config_class)
    register_blueprints(app)
    register_extensions(app)
    register_errorhandlers(app)
    celery.conf.update(app.config)
    return app


def register_extensions(app):
    bcrypt.init_app(app)
    db.init_app(app)
    csrf_protect.init_app(app)
    login.init_app(app)
    migrate.init_app(app, db)
    moment.init_app(app)
    mail.init_app(app)
    return None


def register_blueprints(app):
    app.register_blueprint(main_bp)
    app.register_blueprint(account_bp, url_prefix='/account')
    app.register_blueprint(customers_bp, url_prefix='/customers')
    app.register_blueprint(rentals_bp, url_prefix='/rentals')
    app.register_blueprint(lenses_bp, url_prefix='/lenses')
    app.register_blueprint(newsletter_bp, url_prefix='/newsletter')
    app.register_blueprint(api_bp, url_prefix='/api')
    return None


def register_errorhandlers(app):
    def render_error(error):
        error_code = getattr(error, 'code', 500)
        return render_template('errors/{0}.html'.format(error_code)), error_code
    for errcode in [401, 404, 500]:
        app.errorhandler(errcode)(render_error)
    return None
