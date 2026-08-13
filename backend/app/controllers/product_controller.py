from flask import Blueprint

product_bp = Blueprint("products", __name__)

@product_bp.get("/products")
def get_products():
    return {"message": "Lista de prodcutos"}

