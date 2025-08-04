from utils.security import hash_password, verify_password
from repositories.product_repository import (
    create_product as repo_create, 
    get_all_product as repo_get_all, 
    delete_product as repo_delete, 
    update_product as repo_update,
    get_product_by_id as repo_get_by_id)

def create_product_service(name, description, quantity=0):
    return repo_create(name=name, description=description, quantity=quantity)

def delete_product_service(id):
    return repo_delete(id)

def get_all_product_service(limit):
    return repo_get_all(limit)

def get_product_by_id_service(id):
    return repo_get_by_id(id)

def update_product_service(name, description, quantity=0):
    return repo_update(name, description, quantity)