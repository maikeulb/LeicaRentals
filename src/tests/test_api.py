import pytest
from flask import url_for
from ._factories import CustomerFactory, LensFactory


@pytest.mark.usefixtures('db')
class TestCustomersApi:

    def test_get_customers(self, testapp):
        resp = testapp.get(url_for('api.get_customers'))
        assert resp.status_code == 200

    def test_can_delete(self, testapp, customer):
        resp = testapp.delete(url_for('api.delete_customer', id=customer.id))
        assert resp.status_code == 200


@pytest.mark.usefixtures('db')
class TestLensesApi:

    def test_get_lenses(self, testapp):
        resp = testapp.get(url_for('api.get_lenses'))
        assert resp.status_code == 200

    def test_can_delete(self, testapp, lens):
        resp = testapp.delete(url_for('api.delete_lens', id=lens.id))
        assert resp.status_code == 200


@pytest.mark.usefixtures('db')
class TestRentalsApi:

    def test_get_lenses(self, testapp, rental):
        resp = testapp.get(url_for('api.get_rentals'))
        assert resp.status_code == 200

    def test_can_create_rental(self, testapp, customer, lens):
        resp = testapp.post_json(url_for('api.create_rental'), {
            "customerId": customer.id,
            "lensIds": [lens.id]
        })
        assert resp.status_code == 200

    def test_can_delete(self, testapp, rental):
        resp = testapp.delete(url_for('api.delete_rental', id=rental.id))
        assert resp.status_code == 200


@pytest.mark.usefixtures('db')
class TestAccountApi:

    def test_can_login_rental(self, testapp, user):
        resp = testapp.post_json(url_for('api.login_demo_user'), {
            "username": user.username,
            "password": 'P@ssw0rd!'
        })
        assert resp.status_code == 200
        assert resp.json['result'] == user.id

    def test_can_not_login_rental(self, testapp, user):
        resp = testapp.post_json(url_for('api.login_demo_user'), {
            "username": user.username,
            "password": 'wrong_password'
        }, expect_errors=True)
        assert resp.status_code == 200
        assert resp.json['result'] == 0
