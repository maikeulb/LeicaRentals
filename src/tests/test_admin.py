# from flask import url_for
# from datetime import datetime
# import pytest


# @pytest.mark.usefixtures('db')
# class TestAdmin:

# def test_get_index(user, client, post):
#     client.login_user()
#     resp = client.get(url_for('admin.index'))
#     assert resp.status_code == 200

#     def test_delete_post(user, client, post):
#         client.login_user()
#         resp = client.post(url_for('admin.delete', post_id=post.id))
#         assert resp.status_code == 302
