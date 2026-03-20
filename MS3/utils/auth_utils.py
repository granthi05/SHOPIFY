from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token

bcrypt = Bcrypt()

def hash_password(password):
    return bcrypt.generate_password_hash(password).decode("utf-8")

def check_password(hash, password):
    return bcrypt.check_password_hash(hash, password)

def generate_token(user):
    return create_access_token(identity={
        "id": user.id,
        "email": user.email,
        "role": user.role
    })