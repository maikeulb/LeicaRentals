from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory

from app.extensions import db
from app.models import Customer, MembershipType, User


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class MembershipTypeFactory(BaseFactory):
    name = 'bronze'

    class Meta:
        model = MembershipType


class CustomerFactory(BaseFactory):
    first_name = Sequence(lambda n: 'first_name{0}'.format(n))
    is_signed_up = False
    is_authenticated = True

    membership_type = SubFactory(MembershipTypeFactory)

    class Meta:
        model = User
