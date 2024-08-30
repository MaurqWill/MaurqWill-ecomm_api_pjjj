from database import db
from models.product import Product
from sqlalchemy import select, update, delete

def save_product(product_data):
    new_product = Product(name=product_data['name'], price=product_data['price'])
    db.session.add(new_product)
    db.session.commit()
    db.session.refresh(new_product)
    return new_product

def get_product(product_id):
    query = select(Product).where(Product.id == product_id)
    product = db.session.execute(query).scalar_one_or_none()
    return product

def find_all_products():
    query = select(Product)
    all_products = db.session.execute(query).scalars().all()
    return all_products

def search_product(search_term):
    query = select(Product).where(Product.name.like(f'%{search_term}%'))
    search_products = db.session.execute(query).scalars().all()
    return search_products

def update_product(product_id, data):
    query = (
        update(Product)
        .where(Product.id == product_id)
        .values(**data)
    )
    db.session.execute(query)
    db.session.commit()
    return get_product(product_id)

def delete_product(product_id):
    query = delete(Product).where(Product.id == product_id)
    db.session.execute(query)
    db.session.commit()
