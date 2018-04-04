from flask import url_for
from datetime import datetime
import pytest
from app.models import Lens
from .factories import LensFactory


@pytest.mark.usefixtures('db')
class TestLenses:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('lenses.index'))
        assert resp.status_code == 200

    def test_get_new(self, testapp, membership_type):
        resp = testapp.get(url_for('lenses.new'))
        assert resp.status_code == 200

    def test_get_edit(self, testapp, lens):
        # lens = LensFactory()
        resp = testapp.get(url_for('lenses.edit', id=lens.id))
        assert resp.status_code == 200

    @pytest.mark.skip
    def test_get_details(self, testapp, lens):
        # lens = LensFactory()
        resp = testapp.get(url_for('lenses.details', id=lens.id))
        assert resp.status_code == 200

    def test_can_delete(self, testapp, lens):
        # lens = LensFactory()
        resp = testapp.post(url_for('lenses.delete', id=lens.id))
        assert resp.status_code == 302
