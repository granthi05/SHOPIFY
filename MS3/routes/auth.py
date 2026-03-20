from flask import Blueprint, request, jsonify
from models import User
from database import db
from utils.auth_utils import hash_password, check_password, generate_token

from flask_jwt_extended import jwt_required, get_jwt_identity  # 👈 ADD HERE

auth_bp = Blueprint("auth", __name__)

# 🔹 SIGNUP
@auth_bp.route("/signup", methods=["POST"])
def signup():
    data = request.json

    if User.query.filter_by(email=data["email"]).first():
        return jsonify({"msg": "User already exists"}), 400

    hashed = hash_password(data["password"])

    new_user = User(
        email=data["email"],
        password=hashed,
        role=data.get("role", "user")
    )

    db.session.add(new_user)
    db.session.commit()

    return jsonify({"msg": "User created successfully"})


# 🔹 LOGIN
@auth_bp.route("/login", methods=["POST"])
def login():
    data = request.json

    user = User.query.filter_by(email=data["email"]).first()

    if not user or not check_password(user.password, data["password"]):
        return jsonify({"msg": "Invalid credentials"}), 401

    token = generate_token(user)

    return jsonify({
        "token": token,
        "role": user.role
    })


# 🔐 PROTECTED ROUTE (ADD THIS AT THE END)
@auth_bp.route("/protected", methods=["GET"])
@jwt_required()
def protected():
    user = get_jwt_identity()
    return {"msg": f"Welcome {user['email']}"}