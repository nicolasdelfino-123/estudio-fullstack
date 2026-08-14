from flask import Blueprint
from app.services import product_service

product_bp = Blueprint("products", __name__)

@product_bp.get("/products")
def get_products():
    return product_service.get_all_products()

