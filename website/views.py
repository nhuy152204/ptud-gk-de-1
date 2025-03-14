from flask import Blueprint, render_template, request, flash, redirect, url_for,jsonify
from flask_login import login_required, current_user
from .models import Post, User, Comment
from . import db

views = Blueprint("views", __name__)


@views.route("/")
@views.route("/home")
@login_required
def home():
    posts = Post.query.all()
    return render_template("home.html", user=current_user, posts=posts)


@views.route("/create-post", methods=['GET', 'POST'])
@login_required
def create_post():
    if request.method == "POST":
        text = request.form.get('text')

        if not text:
            flash('Post cannot be empty', category='error')
        else:
            post = Post(text=text, author=current_user.id)
            db.session.add(post)
            db.session.commit()
            flash('Post created!', category='success')
            return redirect(url_for('views.home'))

    return render_template('create_post.html', user=current_user)


@views.route("/delete-post/<id>")
@login_required
def delete_post(id):
    post = Post.query.filter_by(id=id).first()

    if not post:
        flash("Post does not exist.", category='error')
    elif current_user.id != post.id:
        flash('You do not have permission to delete this post.', category='error')
    else:
        db.session.delete(post)
        db.session.commit()
        flash('Post deleted.', category='success')

    return redirect(url_for('views.home'))


@views.route("/posts/<username>")
@login_required
def posts(username):
    user = User.query.filter_by(username=username).first()

    if not user:
        flash('No user with that username exists.', category='error')
        return redirect(url_for('views.home'))

    posts = user.posts
    return render_template("posts.html", user=current_user, posts=posts, username=username)


@views.route("/create-comment/<post_id>", methods=['POST'])
@login_required
def create_comment(post_id):
    text = request.form.get('text')

    if not text:
        flash('Comment cannot be empty.', category='error')
    else:
        post = Post.query.filter_by(id=post_id)
        if post:
            comment = Comment(
                text=text, author=current_user.id, post_id=post_id)
            db.session.add(comment)
            db.session.commit()
        else:
            flash('Post does not exist.', category='error')

    return redirect(url_for('views.home'))


@views.route("/delete-comment/<comment_id>")
@login_required
def delete_comment(comment_id):
    comment = Comment.query.filter_by(id=comment_id).first()

    if not comment:
        flash('Comment does not exist.', category='error')
    elif current_user.id != comment.author and current_user.id != comment.post.author:
        flash('You do not have permission to delete this comment.', category='error')
    else:
        db.session.delete(comment)
        db.session.commit()

    return redirect(url_for('views.home'))

@views.route("/delete-selected-post", methods=["POST"])
@login_required
def delete_selected_posts():
    data = request.get_json()
    post_ids = data.get("ids", [])

    if not post_ids:
        return jsonify({"success": False, "message": "Không có bài viết nào được chọn!"})

    for post_id in post_ids:
        post = Post.query.get(post_id)
        if post and post.author == current_user.id:
            db.session.delete(post)

    db.session.commit()
    return jsonify({"success": True, "message": "Xóa bài viết thành công!"})


@views.route("/delete-selected-comment", methods=["POST"])
@login_required
def delete_selected_comments():
    data = request.get_json()
    comment_ids = data.get("ids", [])

    if not comment_ids:
        return jsonify({"success": False, "message": "Không có bình luận nào được chọn!"})

    for comment_id in comment_ids:
        comment = Comment.query.get(comment_id)
        if comment and (comment.author == current_user.id or comment.post.author == current_user.id):
            db.session.delete(comment)

    db.session.commit()
    return jsonify({"success": True, "message": "Xóa bình luận thành công!"})

@views.route("/profile")
@login_required
def profile():
    return render_template("profile.html", user=current_user)
