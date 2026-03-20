from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
import os

from database import db
from utils.auth_utils import bcrypt
from flask_jwt_extended import JWTManager

from routes.auth import auth_bp

load_dotenv()

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///users.db"
app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["JWT_SECRET_KEY"] = os.getenv("JWT_SECRET")

CORS(app)

db.init_app(app)
bcrypt.init_app(app)
JWTManager(app)

app.register_blueprint(auth_bp, url_prefix="/auth")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)