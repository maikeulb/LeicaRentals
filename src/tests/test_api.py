from flask import url_for
from datetime import datetime
import pytest


# @pytest.mark.usefixtures('db')
# class TestPostApi:

    # def test_get_posts(user, client, post):
    #     client.login_user()
    #     resp = client.get(url_for('api.get_posts'))
    #     assert resp.status_code == 200

    # def test_delete_posts(user, client, post):
    #     client.login_user()
    #     resp = client.delete(url_for('api.delete_post', id=post.id))
    #     assert resp.status_code == 200


# @pytest.mark.usefixtures('db')
# class TestNotificationApi:

    # def test_get_notifications(user, client, post):
    #     client.login_user()
    #     resp = client.get(url_for('api.get_notifications'))
    #     assert resp.status_code == 200

    # def test_reset_notifications(user, client, post):
    #     client.login_user()
    #     resp = client.delete(url_for('api.reset_notifications', id=post.id))
    #     assert resp.status_code == 200


# @pytest.mark.usefixtures('db')
# class TestLikesApi:

    # def test_like(user, client, post):
    #     client.login_user()
    #     resp = client.post(url_for('api.like', id=post.id))
    #     assert resp.status_code == 200

#     def test_unlike(user, client, post):
#         client.login_user()
#         resp = client.delete(url_for('api.unlike', id=post.id))
#         assert resp.status_code == 200


# @pytest.mark.usefixtures('db')
# class TestFollowingsApi:

    # def test_follow(user, client, post):
    #     client.login_user()
    #     resp = client.post(url_for('api.follow', username='demo'))
    #     assert resp.status_code == 200

#     def test_unfollow(user, client, post):
#         client.login_user()
#         resp = client.delete(url_for('api.unfollow', username='demo'))
#         assert resp.status_code == 200
