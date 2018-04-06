import pytest
from flask import url_for


@pytest.mark.usefixtures('db')
class TestMain:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('main.index'))
        assert resp.status_code == 200
