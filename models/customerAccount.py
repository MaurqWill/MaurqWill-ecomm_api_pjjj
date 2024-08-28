from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy import ForeignKey
from models.customer import Customer

class CustomerAccount(Base):
    __tablename__ = 'CustomerAccounts'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(db.String(50), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(db.String(200), nullable=False)
    customer_id: Mapped[int] = mapped_column(ForeignKey('Customers.id'), nullable=False)
    
    customer: Mapped["Customer"] = db.relationship("Customer", backref="account")
