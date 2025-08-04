from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from config import Config
from .utils.extensions import db
from .models.stock_request import StockRequest
from .models.user import User
from .models.product import Product

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)

    with app.app_context():
        db.create_all()

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(debug=True)