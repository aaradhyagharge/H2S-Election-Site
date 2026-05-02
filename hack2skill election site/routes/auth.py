from flask import Blueprint, request, jsonify
from database.models import db, User, UserSession
from utils.security import hash_password, check_password, generate_jwt
import uuid
import datetime

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/api/auth/register', methods=['POST'])
def register():
    data = request.json
    try:
        if User.query.filter_by(email=data['email']).first():
            return jsonify({"error": "Email already registered"}), 400

        new_user = User(
            full_name=data['full_name'],
            email=data['email'],
            phone_number=data.get('phone_number'),
            password_hash=hash_password(data['password']),
            state=data.get('state'),
            epic_number=data.get('epic_number'),
            language_preference=data.get('language_preference', 'en')
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({"message": "User registered successfully"}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500

@auth_bp.route('/api/auth/login', methods=['POST'])
def login():
    data = request.json
    email = data.get('email')
    password = data.get('password')

    user = User.query.filter_by(email=email).first()
    if user and check_password(password, user.password_hash):
        token = generate_jwt(user.user_id)
        
        session_id = str(uuid.uuid4())
        user_session = UserSession(
            session_id=session_id,
            user_id=user.user_id,
            token=token,
            expires_at=datetime.datetime.utcnow() + datetime.timedelta(days=1),
            ip_address=request.remote_addr,
            device_info=request.headers.get('User-Agent')
        )
        user.last_login = datetime.datetime.utcnow()
        db.session.add(user_session)
        db.session.commit()

        return jsonify({
            "message": "Login successful",
            "token": token,
            "user": {
                "id": user.user_id,
                "name": user.full_name,
                "email": user.email,
                "language": user.language_preference
            }
        }), 200

    return jsonify({"error": "Invalid email or password"}), 401
