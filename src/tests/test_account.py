import pytest
from flask import url_for


@pytest.mark.usefixtures('db')
class TestAccount:

    def test_get_register(self, testapp, user):
        res = testapp.get(url_for('account.register'))
        assert res.status_code == 200

    @pytest.mark.skip(reason="requires login, make client fixture")
    def test_redirect_register(self, testapp, user):
        testapp.get(url_for('account.login'))
        res = testapp.get(url_for('account.register'))
        assert res.status_code == 302

    def test_get_login(self, testapp, user):
        res = testapp.get(url_for('account.login'))
        assert res.status_code == 200

    @pytest.mark.skip(reason="requires login, make client fixture")
    def test_redirect_login(self, testapp, user):
        res = testapp.get(url_for('account.login'))
        assert res.status_code == 302

    def test_can_register(self, testapp, user):
        res = testapp.post(url_for('account.register', data=user))
        assert res.status_code == 200

    def test_can_login(self, testapp, user):
        res = testapp.post(url_for('account.register', data=user))
        res = testapp.post(url_for('account.login', data=user))
        assert res.status_code == 200

    def test_can_logout(self, testapp, user):
        res = testapp.get(url_for('account.logout'))
        assert res.status_code == 302
