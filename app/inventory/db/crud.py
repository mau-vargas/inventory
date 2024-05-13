from sqlalchemy.orm import Session
from app.inventory.db.model import Product
from app.inventory.db.schemas import ProductSchema
from app.inventory.db.schemas import Request, Response, RequestBook
from app.mq_supply import producer_supply
from app.mq_dispatcher import producer_dispacher


def get_product_by_code(db: Session, code: int):
    return db.query(Product).filter(Product.code == code).first()


def product_request(db: Session, product: ProductSchema):
    _product = get_product_by_code(db=db, code=product.code)
    if _product.available_quantity < product.count:
        count = product.count - _product.available_quantity
        producer_supply.execute_order(
            count, product.code, product.branch)
        return Response(status="OK",
                        code="200",
                        message="No hay suficientes "+_product.name_product).dict(exclude_none=True)
    else:
        _product.available_quantity = _product.available_quantity - product.count
        producer_dispacher.send_order(
            _product.available_quantity, product.code, product.branch)
        db.commit()
        db.refresh(_product)
        return Response(status="Ok",
                        code="200",
                        message="Quedan "+str(_product.available_quantity) + " unidades en stock.").dict(exclude_none=True)
