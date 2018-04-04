# from flask import url_for
# from datetime import datetime
# import pytest
# from app.models import Post, User


# @pytest.mark.usefixtures('db')
# class TestUser:

#     def test_get_profile(user, client, post):
#         client.login_user()
#         resp = client.get(url_for('user.profile', username='demo'))
#         assert resp.status_code == 200

#     def test_get_edit_profile(user, client, post):
#         client.login_user()
#         resp = client.get(url_for('user.edit_profile'))
#         assert resp.status_code == 200

#     def test_get_discover(user, client, post):
#         client.login_user()
#         resp = client.get(url_for('user.discover'))
#         assert resp.status_code == 200

#     def test_can_edit_profile(user, client, post):
#         client.login_user()
#         user = User(username='demo',
#                     email='demo@example.com',
#                     bio='fummy bio',
#                     profile_img_url='dimmy url')
#         resp = client.post(url_for('posts.post', data=user))
#         assert resp.status_code == 200
