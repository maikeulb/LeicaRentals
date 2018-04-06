import json
from datetime import datetime, date
from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from app.extensions import db
from app.models import (
    Customer,
    MembershipType,
    User,
    Lens,
    Rental,
    Mount,
    FocalLength
)


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class MembershipTypeFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = 'bronze'

    class Meta:
        model = MembershipType


class FocalLengthFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = '35mm'

    class Meta:
        model = FocalLength


class MountFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = 'slr'

    class Meta:
        model = Mount


def _date_handler(obj): return (
    obj.isoformat()
    if isinstance(obj, (datetime, date))
    else None
)


class CustomerFactory(BaseFactory):
    id = Sequence(lambda n: n)
    first_name = Sequence(lambda n: 'first_name{0}'.format(n))
    last_name = Sequence(lambda n: 'last_name{0}'.format(n))
    date_of_birth = json.dumps(datetime.now(), default=_date_handler)
    membership_type = SubFactory(MembershipTypeFactory)

    class Meta:
        model = Customer


class LensFactory(BaseFactory):
    id = Sequence(lambda n: n)
    name = Sequence(lambda n: 'name{0}'.format(n))
    date_added = json.dumps(datetime.now(), default=_date_handler)
    release_date = json.dumps(datetime.now(), default=_date_handler)
    number_in_stock = Sequence(lambda n: n)
    number_available = Sequence(lambda n: n)
    mount = SubFactory(MountFactory)
    focal_length = SubFactory(FocalLengthFactory)

    class Meta:
        model = Lens


class RentalFactory(BaseFactory):
    id = Sequence(lambda n: n)
    date_rented = json.dumps(datetime.now(), default=_date_handler)
    date_returned = json.dumps(datetime.now(), default=_date_handler)
    customer_id = Sequence(lambda n: n)
    lens_id = Sequence(lambda n: n)

    customer = SubFactory(CustomerFactory)
    lens = SubFactory(LensFactory)

    class Meta:
        model = Rental
