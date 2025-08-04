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

def update_product(id, new_product):
    product = Product.query.get(id)

    if not product:
        return False
    
    if "name" in new_product:
        product.name = new_product["name"]
    if "description" in new_product:
        product.description = new_product["description"]
    if "quantity" in new_product:
        product.quantity = new_product["quantity"]
    
    db.session.commit()

def get_product_by_id(id):
    return Product.query.get(id)

def get_all_product(limit):
    query = Product.query
    if limit:
        query = query.limit(limit)
    return query.all()



