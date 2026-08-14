from app.repositories import product_repository


def get_all_products():
    return product_repository.get_all_products()