from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from services.product_service import get_product_by_id_service, create_product_service, get_all_product_service, update_product_service, delete_product_service

product_bp = Blueprint('product', __name__, url_prefix='/products')

@product_bp.route('/', methods=["POST"])
@jwt_required()
def create_product_route():
    data = request.get_json()
    product = create_product_service(
        name=data["name"],
        description=data["description"],
        quantity=data.get("quantity", 0)
    )
    if product:
        return jsonify({"message": "product created"}), 201
    
    return jsonify({"message": "can not create product"}), 400
