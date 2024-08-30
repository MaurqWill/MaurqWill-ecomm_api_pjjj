from database import db
from models.customerAccount import CustomerAccount
from sqlalchemy import select, update, delete

def create_account(data):

    account = CustomerAccount(**data)
    db.session.add(account)
    db.session.commit()
    db.session.refresh(account)
    return account

def get_account(account_id):

    query = select(CustomerAccount).where(CustomerAccount.id == account_id)
    account = db.session.execute(query).scalar_one_or_none()
    return account

def update_account(account_id, data):

    query = (
        update(CustomerAccount)
        .where(CustomerAccount.id == account_id)
        .values(**data)
    )
    db.session.execute(query)
    db.session.commit()
    return get_account(account_id)

def delete_account(account_id):

    query = delete(CustomerAccount).where(CustomerAccount.id == account_id)
    db.session.execute(query)
    db.session.commit()

def find_all_accounts():

    query = select(CustomerAccount)
    all_accounts = db.session.execute(query).scalars().all()
    return all_accounts

def find_all_accounts_paginate(page, per_page):

    query = select(CustomerAccount)
    accounts = db.paginate(query, page=page, per_page=per_page)
    return accounts
