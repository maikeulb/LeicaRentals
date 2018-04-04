import pytest

from app import create_app
from app.models import User, Customer, MembershipType
from app.extensions import db as _db
from webtest import TestApp
from .factories import CustomerFactory, MembershipTypeFactory
from flask import Response, url_for
from flask.testing import FlaskClient
from werkzeug.utils import cached_property


@pytest.fixture
def app():
    _app = create_app('config.TestingConfig')
    ctx = _app.test_request_context()
    ctx.push()

    yield _app

    ctx.pop()


@pytest.fixture(scope='function')
def testapp(app):
    return TestApp(app)


@pytest.fixture
def db(app):
    _db.app = app
    with app.app_context():
        _db.create_all()

    yield _db

    _db.session.close()
    _db.drop_all()


@pytest.fixture
def membership_type(db):
    membership_type = MembershipTypeFactory()
    db.session.commit()
    return membership_type


@pytest.fixture
def customer(db):
    customer = CustomerFactory(first_name='user')
    db.session.commit()
    return user


@pytest.fixture
def user(db):
    user = User(username='demo',
                email='demo@example.com')
    user.set_password('P@ssw0rd!')
    db.session.add(user)
    db.session.commit()
    return user
