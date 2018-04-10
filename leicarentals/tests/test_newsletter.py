import pytest
from flask import url_for


@pytest.mark.usefixtures('db')
class TestNewsletter:

    def test_get_index(self, testapp):
        resp = testapp.get(url_for('newsletter.index'))
        assert resp.status_code == 200

    def test_can_new(self, user, testapp, mount, focal_length):
        resp_news = testapp.get(url_for('newsletter.index'))
        form = resp_news.forms['newsletterForm']
        form['subject'] = "subject"
        form['message'] = "msg"
        resp = form.submit()
        assert resp.status_code == 302
