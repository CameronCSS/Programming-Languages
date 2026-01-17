from flask import Blueprint, request, jsonify
from app import db
from models import User
from flask_security.utils import hash_password

auth_bp = Blueprint("auth", __name__, url_prefix="/auth")

@auth_bp.route("/register", methods=["POST"])
def register():
    data = request.get_json()
    new_user = User(
        email=data["email"],
        password=hash_password(data["password"]),
        active=True
    )
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created"}), 201
