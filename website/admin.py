from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from .models import User, db
from werkzeug.security import generate_password_hash

admin = Blueprint('admin', __name__, url_prefix='/admin')  # ✅ Định nghĩa URL prefix tại đây

@admin.route('/')
@login_required
def admin_dashboard():
    if not current_user.is_admin:
        flash("Bạn không có quyền truy cập!", "danger")
        return redirect(url_for('views.home'))

    users = User.query.all()
    return render_template('admin.html', users=users, user=current_user)  # ✅ Truyền 'user'


@admin.route('/block/<int:user_id>')
@login_required
def block_user(user_id):
    if not current_user.is_admin:
        flash("Bạn không có quyền!", "danger")
        return redirect(url_for('admin.admin_dashboard'))

    user = User.query.get(user_id)
    if user:
        user.is_blocked = True
        db.session.commit()
        flash(f"Tài khoản {user.email} đã bị khóa!", "success")

    return redirect(url_for('admin.admin_dashboard'))

@admin.route('/unblock/<int:user_id>')
@login_required
def unblock_user(user_id):
    if not current_user.is_admin:
        flash("Bạn không có quyền!", "danger")
        return redirect(url_for('admin.admin_dashboard'))

    user = User.query.get(user_id)
    if user:
        user.is_blocked = False
        db.session.commit()
        flash(f"Tài khoản {user.email} đã được mở khóa!", "success")

    return redirect(url_for('admin.admin_dashboard'))

@admin.route('/reset_password/<int:user_id>')
@login_required
def reset_password(user_id):
    if not current_user.is_admin:
        flash("Bạn không có quyền!", "danger")
        return redirect(url_for('admin.admin_dashboard'))

    user = User.query.get(user_id)
    if user:
        new_password = "defaultpassword123"
        user.password = generate_password_hash(new_password, method='pbkdf2:sha256')
        db.session.commit()
        flash(f"Mật khẩu của {user.email} đã được reset thành '{new_password}'!", "success")

    return redirect(url_for('admin.admin_dashboard'))
