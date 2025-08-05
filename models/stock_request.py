from utils.extensions import db
from datetime import datetime

class StockRequest(db.Model):
    __tablename__ = "stock_requests"

    id = db.Column(db.Integer, primary_key=True)
    quantity = db.Column(db.Integer, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey("products.id"), nullable=False)

    status = db.Column(db.Enum("pending", "approved", "rejected"), default="pending")
    request_date = db.Column(db.DateTime, default=datetime.now)

    user = db.relationship("User", back_populates="stock_requests")
    product = db.relationship("Product", back_populates="stock_requests")
