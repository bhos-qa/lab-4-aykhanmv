# controller.py
from app import app
from flask import Blueprint, request, jsonify
from models import db, User, Class, Enrollment, Notification

@app.route('/')
def index():
    return jsonify({'message': 'Welcome to our University PMS API!'})


@app.route('/register', methods=['POST'])
def register():
    data = request.get_json()

    # Check if the username is already taken
    existing_user = User.query.filter_by(username=data['username']).first()
    if existing_user:
        return jsonify({'message': 'Username is already taken!'}), 400

    # Create a new user
    new_user = User(username=data['username'], password=data['password'], email=data['email'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({'message': 'User registered successfully!'}), 201


@app.route('/login', methods=['POST'])
def login():
    data = request.get_json()

    # Check if username and password are provided
    if not data.get('username') or not data.get('password'):
        return jsonify({'message': 'Username and password are required!'}), 400

    user = User.query.filter_by(username=data['username'], password=data['password']).first()
    if user:
        return jsonify({'message': 'Login successful!', 'user_id': user.id}), 200

    return jsonify({'message': 'Invalid credentials!'}), 401


@app.route('/profile/<int:user_id>', methods=['GET'])
def get_profile(user_id):
    if user_id is None:  # This will not trigger normally with Flask routing
        return jsonify({'message': 'User ID is required!'}), 400

    user = User.query.get(user_id)
    if user:
        return jsonify({'id': user.id, 'username': user.username, 'email': user.email}), 200
    return jsonify({'message': 'User not found!'}), 404


@app.route('/password-reset', methods=['POST'])
def password_reset():
    data = request.get_json()

    # Check if email and new_password are provided
    if not data.get('email') or not data.get('new_password'):
        return jsonify({'message': 'Email and new password are required!'}), 400

    user = User.query.filter_by(email=data['email']).first()
    if user:
        user.password = data['new_password']
        db.session.commit()
        return jsonify({'message': 'Password reset successfully!'}), 200
    return jsonify({'message': 'User not found!'}), 404


@app.route('/profile/<int:user_id>', methods=['PUT'])
def update_profile(user_id):
    # Check if user_id is a valid integer
    if not isinstance(user_id, int):
        return jsonify({'message': 'ID must be a number!'}), 400

    data = request.get_json()
    user = User.query.get(user_id)
    if user:
        if data.get('username') is not None:
            user.username = data['username']
        
        if data.get('email') is not None:
            user.email = data['email']
        
        db.session.commit()
        return jsonify({'message': 'Profile updated successfully!'}), 200
    return jsonify({'message': 'User not found!'}), 404


@app.route('/profile/<int:user_id>', methods=['DELETE'])
def remove_profile(user_id):
    # Check if user_id is valid (non-zero and positive)
    if user_id is None:
        return jsonify({'message': 'ID is required!'}), 400

    user = User.query.get(user_id)
    if user:
        db.session.delete(user)
        db.session.commit()
        return jsonify({'message': 'Profile deleted successfully!'}), 200

    return jsonify({'message': 'User not found!'}), 404


@app.route('/join_class/<int:user_id>/<int:class_id>', methods=['POST'])
def join_class(user_id, class_id):
    # Check if user_id and class_id are valid
    if user_id is None or class_id is None:
        return jsonify({'message': 'User ID and Class ID are required!'}), 400
    
    enrollment = Enrollment(user_id=user_id, class_id=class_id)
    db.session.add(enrollment)
    db.session.commit()
    return jsonify({'message': 'Successfully joined class!'}), 201


@app.route('/leave_class/<int:user_id>/<int:class_id>', methods=['DELETE'])
def leave_class(user_id, class_id):
    # Check if user_id and class_id are valid
    if user_id is None or class_id is None:
        return jsonify({'message': 'User ID and Class ID are required!'}), 400

    enrollment = Enrollment.query.filter_by(user_id=user_id, class_id=class_id).first()
    if enrollment:
        db.session.delete(enrollment)
        db.session.commit()
        return jsonify({'message': 'Successfully left class!'}), 200
    return jsonify({'message': 'Not enrolled in this class!'}), 404


@app.route('/classes', methods=['GET'])
def get_classes():
    classes = Class.query.all()
    return jsonify([{'id': cls.id, 'name': cls.name, 'description': cls.description} for cls in classes]), 200
