from flask import render_template, Blueprint, request
from puppy_company.models import ForumPost

core = Blueprint('core', __name__)


@core.route('/')
def index():
    page = request.args.get('page', 1, type=int)
    forum_posts = ForumPost.query.order_by(ForumPost.date.desc()).paginate(page=page, per_page=10)
    return render_template('index.html', forum_posts=forum_posts)


@core.route('/info')
def info():
    return render_template('info.html')
