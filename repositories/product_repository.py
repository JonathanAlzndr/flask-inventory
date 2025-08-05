from utils.extensions import db
from models.product import Product

def create_product(name, description, quantity):
    product = Product(name=name, description=description, quantity=quantity)
    db.session.add(product)
    db.session.commit()
    return product

def delete_product(id):
    product = Product.query.get(id)

    if not product:
        return False
    
    db.session.delete(product)
    db.session.commit()

    return True

def update_product(id, name, description, quantity):
    product = Product.query.get(id)

    if not product:
        return False
    
    if name is not None:
        product.name = name
    if description is not None:
        product.description = description
    if quantity is not None:
        product.quantity = quantity
    
    db.session.commit()
    return True

def get_product_by_id(id):
    return Product.query.get(id)

def get_all_product(limit: int = 10, offset: int = 0):
    return Product.query.offset(offset=offset).limit(limit=limit).all()


