from database import db
from models.customerAccount import CustomerAccount
from sqlalchemy import select, update, delete

def create_account(data):
    """
    Create a new customer account.
    """
    account = CustomerAccount(**data)
    db.session.add(account)
    db.session.commit()
    db.session.refresh(account)
    return account

def get_account(account_id):
    """
    Retrieve a customer account by ID.
    """
    query = select(CustomerAccount).where(CustomerAccount.id == account_id)
    account = db.session.execute(query).scalar_one_or_none()
    return account

def update_account(account_id, data):
    """
    Update customer account details based on their ID.
    """
    query = (
        update(CustomerAccount)
        .where(CustomerAccount.id == account_id)
        .values(**data)
    )
    db.session.execute(query)
    db.session.commit()
    return get_account(account_id)

def delete_account(account_id):
    """
    Delete a customer account from the database based on their ID.
    """
    query = delete(CustomerAccount).where(CustomerAccount.id == account_id)
    db.session.execute(query)
    db.session.commit()

def find_all_accounts():
    """
    Retrieve all customer accounts.
    """
    query = select(CustomerAccount)
    all_accounts = db.session.execute(query).scalars().all()
    return all_accounts

def find_all_accounts_paginate(page, per_page):
    """
    Retrieve customer accounts with pagination.
    """
    query = select(CustomerAccount)
    accounts = db.paginate(query, page=page, per_page=per_page)
    return accounts
