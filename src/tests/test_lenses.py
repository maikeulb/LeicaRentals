import pytest
from flask import url_for
from datetime import datetime, date


def _date_handler(obj): return (
    obj.isoformat()
    if isinstance(obj, (datetime, date))
    else None
)


@pytest.mark.usefixtures('db')
class TestLenses:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('lenses.index'))
        assert resp.status_code == 200

    def test_get_new(self, testapp, membership_type):
        resp = testapp.get(url_for('lenses.new'))
        assert resp.status_code == 200

    def test_get_edit(self, testapp, lens):
        resp = testapp.get(url_for('lenses.edit', id=lens.id))
        assert resp.status_code == 200

    @pytest.mark.skip
    def test_get_details(self, testapp, lens):
        # lens = LensFactory()
        resp = testapp.get(url_for('lenses.details', id=lens.id))
        assert resp.status_code == 200

    # def test_can_new(self, user, testapp, mount, focal_length):
    #     resp_lens = testapp.get(url_for('lenses.new'))
    #     form = resp_lens.forms["newLensForm"]
    #     form['name'] = "summicron"
    #     form['release_date'] = json.dumps(
    #         datetime.now(), default=_date_handler)
    #     form['number_in_stock'] = 3
    #     form['mount_id'] = mount.id
    #     form['focal_length_id'] = focal_length.id
    #     resp = form.submit()
    #     assert resp.status_code == 302

    # def test_can_edit(self, user, testapp, lens, mount, focal_length):
    #     resp = testapp.get(url_for('lenses.new', id=lens.id))
    #     form = resp.forms[0]
    #     form['name'] = "summitar"
    #     form['release_date'] = json.dumps(
    #         datetime.now(), default=_date_handler)
    #     form['number_in_stock'] = 3
    #     form['mount_id'] = mount.id
    #     form['focal_length_id'] = focal_length.id
    #     assert resp.status_code == 200

    def test_can_delete(self, testapp, lens):
        resp = testapp.post(url_for('lenses.delete', id=lens.id))
        assert resp.status_code == 302
