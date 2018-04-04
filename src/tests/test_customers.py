from flask import url_for
from datetime import datetime
import pytest
from app.models import Customer
from .factories import CustomerFactory


@pytest.mark.usefixtures('db')
class TestLenses:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('customers.index'))
        assert resp.status_code == 200

    def test_get_new(self, testapp, membership_type):
        resp = testapp.get(url_for('customers.new'))
        assert resp.status_code == 200

    def test_get_edit(self, testapp, customer):
        customer = CustomerFactory()
        resp = testapp.get(url_for('customers.edit', id=customer.id))
        assert resp.status_code == 200

    @pytest.mark.skip
    def test_get_details(self, testapp, customer):
        # customer = CustomerFactory()
        resp = testapp.get(url_for('customers.details', id=customer.id))
        assert resp.status_code == 200

    def test_get_newsletter(self, testapp):
        resp = testapp.get(url_for('customers.newsletter'))
        assert resp.status_code == 302

    def test_can_delete(self, testapp, customer):
        # customer = CustomerFactory()
        resp = testapp.post(url_for('customers.delete', id=customer.id))
        assert resp.status_code == 302
