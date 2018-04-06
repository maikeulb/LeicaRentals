import pytest

from app import create_app
from app.models import (
    User,
    Customer,
    MembershipType,
    Lens,
    Mount,
    Rental,
    FocalLength
)
from app.extensions import db as _db
from webtest import TestApp
from ._factories import (
    CustomerFactory,
    MembershipTypeFactory,
    MountFactory,
    FocalLengthFactory,
    LensFactory,
    RentalFactory
)
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


@pytest.fixture(scope='function')
def membership_type(db):
    membership_type = MembershipTypeFactory()
    db.session.commit()
    return membership_type


@pytest.fixture(scope='function')
def customer(db):
    customer = CustomerFactory()
    db.session.commit()
    return customer


@pytest.fixture(scope='function')
def lens(db):
    lens = LensFactory()
    db.session.commit()
    return lens


@pytest.fixture(scope='function')
def mount(db):
    mount = MountFactory()
    db.session.commit()
    return mount


@pytest.fixture(scope='function')
def focal_length(db):
    mount = FocalLengthFactory()
    db.session.commit()
    return mount


@pytest.fixture(scope='function')
def rental(db, customer, lens):
    rental = RentalFactory(customer_id=customer.id,
                           lens_id=lens.id)
    db.session.commit()
    return rental


@pytest.fixture(scope='function')
def user(db):
    user = User(username='demo',
                email='demo@example.com')
    user.set_password('P@ssw0rd!')
    db.session.add(user)
    db.session.commit()
    return user
