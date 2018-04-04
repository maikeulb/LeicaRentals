from flask import url_for
from datetime import datetime
import pytest


@pytest.mark.usefixtures('db')
class TestNewsletter:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('rentals.index'))
        assert resp.status_code == 200

    def test_get_new(self, testapp):
        resp = testapp.get(url_for('rentals.new'))
        assert resp.status_code == 200

    def test_can_new(self, testapp):
        resp = testapp.post(url_for('rentals.new'))
        assert resp.status_code == 200
