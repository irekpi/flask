from flask import render_template, redirect, request, flash, url_for, Blueprint, abort
from flask_login import current_user, login_required
from puppy_company import db
from puppy_company.models import ForumPost
from puppy_company.forum_post.forms import ForumPostForm


forum_posts = Blueprint('forum_posts', __name__)

# Create
@forum_posts.route('/create', methods=['GET', 'POST'])
def create_post():
    form = ForumPostForm()
    if form.validate_on_submit():
        forum_post = ForumPost(title=form.title.data,
                               text=form.text.data,
                               user_id=current_user.id)
        db.session.add(forum_post)
        db.session.commit()
        flash('Post was created')
        return redirect(url_for('core.index'))
    return render_template('create_post.html', form=form)

# View
@forum_posts.route('/<int:forum_post_id>')
def forum_post(forum_post_id):
    forum_post = ForumPost.query.get_or_404(forum_post_id)
    return render_template('forum_post.html', title=forum_post.title,
                           date=forum_post.date, post=forum_post)

# Edit
@forum_posts.route('/<int:forum_post_id>/update', methods=['GET', 'POST'])
@login_required
def update_post(forum_post_id):
    forum_post = ForumPost.query.get_or_404(forum_post_id)

    if forum_post.author != current_user:
        abort(403)

    form = ForumPostForm()
    if form.validate_on_submit():
        forum_post.title = form.title.data
        forum_post.text = form.text.data

        db.session.commit()
        flash('Post updated!')
        return redirect(url_for('forum_posts.forum_post', forum_post_id=forum_post.id))
    elif request.method == 'GET':
        form.title.data = forum_post.title
        form.text.data = forum_post.text
    return render_template('create_post.html', title='Updating', form=form)

# Del
@forum_posts.route('/<int:forum_post_id>/delete', methods=['POST'])
@login_required
def delete_post(forum_post_id):
    forum_post = ForumPost.query.get_or_404(forum_post_id)
    if forum_post.author != current_user:
        abort(403)

    db.session.delete(forum_post)
    db.session.commit()
    flash('Deleted')
    return redirect(url_for('core.index'))
