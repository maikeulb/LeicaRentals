import sys
from datetime import datetime
from flask import (
    render_template,
    flash,
    redirect,
    url_for,
    request,
    jsonify,
    current_app
)
from flask_login import current_user, login_required
from app.extensions import db
from app.api import api
from app.models import (
    Post,
    User,
    Notification,
    UserNotification
)
import json
from app.api.forms import (
    CommentForm,
)
from app.models import (
    Post,
    Comment,
)

@api.route('/follow/<username>')
@login_required
def follow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        flash('User not found.')
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot follow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.follow(user)
    db.session.commit()
    return jsonify({'result': 'success'})


@api.route('/unfollow/<username>')
@login_required
def unfollow(username):
    user = User.query.filter_by(username=username).first()
    if user is None:
        return redirect(url_for('main.index'))
    if user == current_user:
        flash('You cannot unfollow yourself!')
        return redirect(url_for('main.user', username=username))
    current_user.unfollow(user)
    db.session.commit()
    return redirect(url_for('main.user', username=username))


@api.route('/like/<id>', methods=['GET', 'POST'])
@login_required
def like(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        flash('User not found.')
        return redirect(url_for('main.index'))
    current_user.like(post)
    user = User.query.filter_by(id=post.user_id).first_or_404()
    user.add_notification('unread_message_count', user.new_messages())
    notification = UserNotification(author=current_user, recipient=user, body=1)
    db.session.add(notification)
    db.session.commit()
    return jsonify({
        'data': current_user.username})


@api.route('/unlike/<id>', methods=['GET', 'POST'])
@login_required
def unlike(id):
    post = Post.query.filter_by(id=id).first()
    if post is None:
        flash('User not found.')
        return redirect(url_for('main.index'))
    current_user.unlike(post)
    db.session.commit()
    return jsonify({
        'data': current_user.username})


@api.route('/notifications')
@login_required
def notifications():
    since = request.args.get('since', 0.0, type=float)
    notifications = current_user.notifications.filter(
        Notification.timestamp > since).order_by(Notification.timestamp.asc())
    return jsonify([{
        'name': n.name,
        'data': n.get_data(),
        'timestamp': n.timestamp
    } for n in notifications])


@api.route('/comment/<id>', methods=['post'])
def comment(id):
    post = Post.query.filter_by(id=id).first_or_404()
    form = CommentForm()
    print(form, sys.stdout)
    print(post, sys.stdout)
    if form.validate_on_submit():
        comment = Comment(body=form.body.data,
                          post=post,
                          author=current_user._get_current_object())
        db.session.add(comment)
        db.session.commit()
        print(form.body.data, sys.stdout)
        return jsonify({
            'data': form.body.data})
    return jsonify(data=form.errors)
