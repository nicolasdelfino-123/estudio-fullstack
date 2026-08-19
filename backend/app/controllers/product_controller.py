from flask import Blueprint, request, jsonify
from app.services import product_service

product_bp = Blueprint("products", __name__)

@product_bp.get("/products")
def get_products():
    return product_service.get_all_products()

@product_bp.get("/products/<int:id>")
def get_by_id(id):
    product = product_service.get_by_id(id)
    if product is None:
        return jsonify({"error": "producto no encontrado"}), 404

    return jsonify(product.serialize()), 200



@product_bp.post("/products")
def create_product():
    data = request.get_json()
    product = product_service.create_product(data)

    return jsonify(product.serialize()), 201
