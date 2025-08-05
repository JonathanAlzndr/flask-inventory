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

@product_bp.route('/<int:product_id>', methods=['GET'])
@jwt_required()
def get_product_by_id(product_id):
    product = get_product_by_id_service(product_id)

    if product:
        return jsonify({"id": product.id, 
                        "name": product.name, 
                        "description": f"{product.description}", 
                        "quantity": product.quantity}), 200
    else:
        return jsonify({"message": "product not found"}), 404
    
@product_bp.route('/<int:product_id>', methods=['DELETE'])
@jwt_required()
def delete_product_by_id(product_id):
    result = delete_product_service(product_id)

    if result == True:
        return jsonify({"message": "Product deleted"}), 200
    else:
        return jsonify({"message": "Product not found"}), 404
    
@product_bp.route('/', methods=['GET'])
@jwt_required()
def get_all_products():

    limit = request.args.get('limit', 10, type=int)
    offset = request.args.get('offset', 0, type=int)

    products = get_all_product_service(limit, offset)

    result = [
        {
            "id": p.id,
            "name": p.name,
            "description": p.description,
            "quantity": p.quantity
        }
        for p in products
    ]

    return jsonify(result), 200

@product_bp.route('/<int:product_id>', methods=['PATCH'])
@jwt_required()
def update_product(product_id):

    data = request.get_json()

    if not data:
        return jsonify({"message": "Invalid or missing JSON body"}), 400

    name = data.get('name')
    description = data.get('description')
    quantity = data.get('quantity')

    result = update_product_service(product_id, name, description, quantity)

    if result:
        return jsonify({"message": "Product updated successfully"}), 200
    else:
        return jsonify({"message": "Failed to update product"}), 400
