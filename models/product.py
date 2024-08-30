from typing import List
from database import db, Base
from sqlalchemy.orm import Mapped, mapped_column, relationship
from models.orderProduct import order_product

class Product(Base):
    __tablename__ = 'Products'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(db.String(255), nullable=False)
    price: Mapped[float] = mapped_column(db.Float, nullable=False)
    
    # Many-To-Many: Products and Orders
    orders: Mapped[List["Order"]] = relationship("Order", secondary=order_product, back_populates="products", lazy="select")