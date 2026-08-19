from app.repositories import product_repository


def get_all_products():
    return product_repository.get_all_products()

def create_product(data):
    stock = int(data["stock"])

    if stock < 0:
        raise ValueError("el stock no puede ser cero")

    return product_repository.create_product(data)

def get_by_id(id):
    return product_repository.get_by_id(id)
