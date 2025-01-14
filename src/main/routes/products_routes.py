from flask import Blueprint, jsonify

products_routes_bp = Blueprint("products_routes", __name__)

@products_routes_bp.route("/products", methods=["POST"])
def insert_product():
    return jsonify({"message": "Product created successfully"}), 200

@products_routes_bp.route("/products/<product_name>", methods=["GET"])
def get_product(product_name):
    return jsonify({"msg":f"produto {product_name}"}), 200

