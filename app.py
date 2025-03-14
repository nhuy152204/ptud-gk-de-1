from website import create_app, db
from website.models import User
from werkzeug.security import generate_password_hash

app = create_app()

def create_admin():
    with app.app_context():  # ✅ Đảm bảo có app context
        admin_email = "admin@example.com"
        admin_username = "admin"
        admin_password = "admin123"

        if not User.query.filter_by(email=admin_email).first():
            admin_user = User(
                email=admin_email,
                username=admin_username,
                password=generate_password_hash(admin_password, method='pbkdf2:sha256'),
                is_admin=True
            )
            db.session.add(admin_user)
            db.session.commit()
            print("✅ Admin user created!")
        else:
            print("⚠️ Admin user already exists!")

if __name__ == "__main__":
    with app.app_context():  # ✅ Đảm bảo context trước khi tạo database
        db.create_all()
        create_admin()  
    app.run(debug=True)
