from factory import PostGenerationMethodCall, Sequence, SubFactory
from factory.alchemy import SQLAlchemyModelFactory
from app.extensions import db
from app.models import Customer, MembershipType, User, Lens, Mount


class BaseFactory(SQLAlchemyModelFactory):
    class Meta:
        abstract = True
        sqlalchemy_session = db.session


class MembershipTypeFactory(BaseFactory):
    id = Sequence(lambda n: '{0}'.format(n))
    name = 'bronze'

    class Meta:
        model = MembershipType


class MountFactory(BaseFactory):
    id = Sequence(lambda n: '{0}'.format(n))
    name = '35mm'

    class Meta:
        model = Mount


class CustomerFactory(BaseFactory):
    id = Sequence(lambda n: '{0}'.format(n))
    first_name = Sequence(lambda n: 'first_name{0}'.format(n))

    membership_type = SubFactory(MembershipTypeFactory)

    class Meta:
        model = Customer


class LensFactory(BaseFactory):
    id = Sequence(lambda n: '{0}'.format(n))
    name = Sequence(lambda n: 'name{0}'.format(n))

    mount = SubFactory(MountFactory)

    class Meta:
        model = Lens
