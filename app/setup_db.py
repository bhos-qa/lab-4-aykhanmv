# setup_db.py
from flask import Flask
from models import db, User, Class, Enrollment, Notification

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///university_pms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

def create_db():
    with app.app_context():
        db.create_all()

        # Users
        users = [
            User(username='john_doe', password='password123', email='john@example.com'),
            User(username='jane_smith', password='password123', email='jane@example.com'),
            User(username='alice_wonder', password='password123', email='alice@example.com')
        ]
        db.session.bulk_save_objects(users)

        # Classes
        classes = [
            Class(name='Mathematics 101', description='Introduction to Mathematics.'),
            Class(name='Physics 101', description='Introduction to Physics.'),
            Class(name='Computer Science 101', description='Introduction to Computer Science.')
        ]
        db.session.bulk_save_objects(classes)

        # Enrollments
        enrollments = [
            Enrollment(user_id=1, class_id=1),
            Enrollment(user_id=1, class_id=2),
            Enrollment(user_id=2, class_id=3),
            Enrollment(user_id=3, class_id=1),
        ]
        db.session.bulk_save_objects(enrollments)

        # Notifications
        notifications = [
            Notification(user_id=1, message='Welcome to the University!'),
            Notification(user_id=2, message='Your class Physics 101 starts next week.'),
            Notification(user_id=3, message='You have a new assignment in Mathematics 101.')
        ]
        db.session.bulk_save_objects(notifications)

        db.session.commit()
        print("Database created and populated with dummy data.")

if __name__ == '__main__':
    create_db()
