from app.models.product import Product
from app import db

def get_all_products():
    return Product.query.all()

def create_product(data):
    product = Product(
        nombre=data["nombre"],
        precio=data["precio"],
        stock=data["stock"]
    )

    db.session.add(product)
    db.session.commit()

    return product

def get_by_id(id):
    return db.session.get(Product, id)

