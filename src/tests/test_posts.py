# from flask import url_for
# from datetime import datetime
# import pytest
# from app.models import Post


# @pytest.mark.usefixtures('db')
# class TestPosts:

    # def test_get_index(user, client, post):
    #     client.login_user()
    #     resp = client.get(url_for('posts.index'))
    #     assert resp.status_code == 200

    # def test_get_post(user, client, post):
    #     client.login_user()
    #     resp = client.get(url_for('posts.post'))
    #     assert resp.status_code == 200

    # def test_get_favorites(user, client, post):
    #     client.login_user()
    #     resp = client.get(url_for('posts.favorites'))
    #     assert resp.status_code == 200

    # def test_can_post(user, client, post):
    #     client.login_user()
    #     post = Post(caption='caption',
    #                 photo_filename='filename',
    #                 photo_url='url',
    #                 user_id=1)
    #     resp = client.post(url_for('posts.post', data=post))
    #     assert resp.status_code == 200

    # def test_can_login(self, user, testapp):
    #     res = testapp.post(url_for('account.register', data=user))
    #     res = testapp.post(url_for('account.login', data=user))
    #     assert res.status_code == 200

# #     def test_get_details(user, client, post):
# #         client.login_user()
# #         resp = client.get(url_for('posts.details', id=post.id))
# #         assert resp.status_code == 200
