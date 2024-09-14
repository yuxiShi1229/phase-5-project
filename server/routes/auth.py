from flask import Blueprint, request, jsonify
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity
from models import User
from extensions import db
import logging

bp = Blueprint('auth', __name__)

@bp.route('/signup', methods=['POST'])
def signup():
    if not request.is_json:
        return jsonify({"error": "Request must be JSON"}), 400
    
    data = request.get_json()
    logging.info(f"Received signup data: {data}")

    # Check if email is already registered
    if User.query.filter_by(email=data['email']).first():
        return jsonify({"error": "Email already registered"}), 400

    # Create a new user
    try:
        new_user = User(
            username=data['username'], 
            email=data['email'], 
            is_teacher=data.get('isTeacher', False)
        )
        new_user.set_password(data['password'])

        db.session.add(new_user)
        db.session.commit()

        # Generate JWT token
        access_token = create_access_token(identity=new_user.id)
        return jsonify({"message": "User created successfully", "access_token": access_token}), 201
    except Exception as e:
        logging.error(f"Error during signup: {str(e)}")
        return jsonify({"error": "An error occurred during signup"}), 500

@bp.route('/login', methods=['POST'])
def login():
    data = request.json
    logging.info(f"Received login data: {data}")

    # Find user by email
    user = User.query.filter_by(email=data['email']).first()
    if not user or not user.check_password(data['password']):
        return jsonify({"error": "Invalid email or password"}), 401

    try:
        # Generate JWT token
        access_token = create_access_token(identity=user.id)
        logging.info(f"Login successful for user: {user.id}")
        return jsonify({"message": "Login successful", "access_token": access_token}), 200
    except Exception as e:
        logging.error(f"Error during login: {str(e)}")
        return jsonify({"error": "An error occurred during login"}), 500

@bp.route('/profile', methods=['GET'])
@jwt_required()
def profile():
    user_id = get_jwt_identity()
    user = User.query.get(user_id)

    if user:
        return jsonify({
            "id": user.id,
            "username": user.username,
            "email": user.email,
            "is_teacher": user.is_teacher
        }), 200
    else:
        return jsonify({"error": "User not found"}), 404

