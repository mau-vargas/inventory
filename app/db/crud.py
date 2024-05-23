from sqlalchemy.orm import Session
from db.model import Product
from db.schemas import ProductSchema
from db.schemas import Request, Response
from mq_supply import producer_supply
from mq_dispatcher import producer_dispacher


def get_product_by_code(db: Session, code: int):
    return db.query(Product).filter(Product.code == code).first()


def product_request(db: Session, product: ProductSchema):
    _product = get_product_by_code(db=db, code=product.code)

    if _product is None:
        return None, None

    elif _product.available_quantity < product.count:
        count = product.count - _product.available_quantity
        producer_supply.execute_order(
            count, product.code, product.branch)
        has_stock = False
        return _product, has_stock

    else:
        _product.available_quantity = _product.available_quantity - product.count
        producer_dispacher.send_order(
            product.count, product.code, product.branch)
        db.commit()
        db.refresh(_product)
        has_stock = True
        return _product, has_stock
