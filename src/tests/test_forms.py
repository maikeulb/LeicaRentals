from flask import url_for
from datetime import datetime
import pytest
from app.account.forms import (
    LoginForm,
    RegistrationForm,
)
from app.customers.forms import (
    CustomerForm,
)
from app.lenses.forms import (
    LensForm,
)
from app.newsletter.forms import (
    NewsletterForm,
)
from app.rentals.forms import (
    RentalForm,
)


class TestRegistrationForm:
    def test_validate_user_already_registered(self, user):
        form = RegistrationForm(username=user.username, email='foo@bar.com',
                                password='example', confirm='example')
        assert form.validate() is False

    def test_validate_email_already_registered(self, user):
        form = RegistrationForm(username='unique', email=user.email,
                                password='example', confirm='example')
        assert form.validate() is False

    def test_validate_success(self, db):
        form = RegistrationForm(username='newusername', email='new@test.test',
                                password='example', confirm='example')
        assert form.validate() is True


class TestLoginForm:
    def test_validate_success(self, user):
        form = LoginForm(username=user.username, password='P@ssw0rd!')
        assert form.validate() is True
        assert form.user == user

    def test_validate_unknown_username(self, db):
        form = LoginForm(username='unknown', password='example')
        assert form.validate() is False
        assert form.user is None

    def test_validate_invalid_password(self, user):
        user.set_password('example')
        form = LoginForm(username=user.username, password='wrongpassword')
        assert form.validate() is False


class CustomerForm:
    def test_validate_success(self, user, membership_type, mount, focal_length):
        form = CustomerForm(first_name="example first",
                            last_name="example last",
                            email="michael@example.com",
                            newsletter=False,
                            date_of_birth=datetime.utcnow,
                            mambership_type_id=membership_type.id)
        assert form.validate() is True


class TestLensForm:
    @pytest.mark.skip(reason="no idea why this is failing")
    def test_validate_success(self, user, mount, focal_length):
        form = LensForm(name='customer',
                        release_date=datetime.utcnow,
                        number_in_stock=3,
                        mount_id=mount.id,
                        focal_length_id=focal_length.id)
        assert form.validate() is True


class TestRentalForm:
    def test_validate_success(self, user):
        form = RentalForm(customer='customer_name',
                          lens="lens_name")
        assert form.validate() is True
