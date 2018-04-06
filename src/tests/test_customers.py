from flask import url_for
from datetime import datetime, date
import pytest
from app.models import Customer
from ._factories import CustomerFactory
import json


def _date_handler(obj): return (
    obj.isoformat()
    if isinstance(obj, (datetime, date))
    else None
)


@pytest.mark.usefixtures('db')
class TestCustomers:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('customers.index'))
        assert resp.status_code == 200

    def test_get_new(self, testapp, membership_type):
        resp = testapp.get(url_for('customers.new'))
        assert resp.status_code == 200

    def test_get_edit(self, testapp, customer):
        resp = testapp.get(url_for('customers.edit', id=customer.id))
        assert resp.status_code == 200

    @pytest.mark.skip
    def test_get_details(self, testapp, customer):
        resp = testapp.get(url_for('customers.details', id=customer.id))
        assert resp.status_code == 200

    def test_get_newsletter(self, testapp):
        resp = testapp.get(url_for('customers.newsletter'))
        assert resp.status_code == 302

    def test_can_new(self, testapp, membership_type):
        resp = testapp.post(url_for('customers.new'))
        assert resp.status_code == 200

    # def test_can_new(self, user, testapp, membership_type):
    #     resp_customer = testapp.get(url_for('customers.new'))
    #     form = resp_customer.forms['newCustomerForm']
    #     form['first_name'] = "first_name_example",
    #     form['last_name'] = "last_name_example",
    #     form['email'] = "test@example.com",
    #     form['newsletter'] = False,
    #     form['date_of_birth'] = json.dumps(
    #         datetime.now(), default=_date_handler),
    #     form['membership_type_id'] = membership_type.id
    #     resp = form.submit()
    #     assert resp.status_code == 302

    def test_can_edit(self, testapp, customer):
        resp = testapp.post(url_for('customers.edit', id=customer.id))
        assert resp.status_code == 200

    # def test_can_edit(self, user, testapp, membership_type):
    #     resp_customer = testapp.get(url_for('customers.new'))
    #     form = resp_customer.forms['newCustomerForm']
    #     form['first_name'] = "first_name_example",
    #     form['last_name'] = "last_name_example",
    #     form['email'] = "test@example.com",
    #     form['newsletter'] = False,
    #     form['date_of_birth'] = json.dumps(
    #         datetime.now(), default=_date_handler),
    #     form['membership_type_id'] = membership_type.id
    #     resp = form.submit()
    #     assert resp.status_code == 302

    def test_can_delete(self, testapp, customer):
        # customer = CustomerFactory()
        resp = testapp.post(url_for('customers.delete', id=customer.id))
        assert resp.status_code == 302
