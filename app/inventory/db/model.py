from sqlalchemy import Column, Integer, String
from app.inventory.db.config import Base


class Product(Base):
    __tablename__ = "inventory"

    product_id = Column(Integer, primary_key=True, index=True)
    code = Column(Integer)
    name_product = Column(String)
    category = Column(String)
    available_quantity = Column(Integer)
    unit_price = Column(String)
    supplier = Column(String)
    entry_date = Column(String)
    update_date = Column(String)
    detail = Column(String)
