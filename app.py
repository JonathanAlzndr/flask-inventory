from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from utils.extensions import db
from models.stock_request import StockRequest
from models.user import User
from models.product import Product
from routes.auth.auth_routes import auth_bp
from routes.product.product_routes import product_bp
from utils.extensions import bcrypt, jwt

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    bcrypt.init_app(app)
    db.init_app(app)
    jwt.init_app(app)

    app.register_blueprint(auth_bp)
    app.register_blueprint(product_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)