from fastapi import APIRouter
from pydantic import BaseModel
from app.inventory.db.config import SessionLocal
import app.inventory.db.crud as crud
from app.inventory.db.schemas import Request, Response, RequestBook
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


class Product(BaseModel):
    code: int
    name: str | None = None
    category: str | None = None
    count: int
    branch: str


class ListProduct(BaseModel):
    list_product: List[Product]


@router.get("/test/test")
async def supply_request(list_product: ListProduct):
    for product in list_product:
        print(product)
    return list_product


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.post("/product_request")
async def supply_request(list_product: ListProduct, db: Session = Depends(get_db)):

    for product in list_product.list_product:
        _product, has_stock = crud.product_request(db, product)
        if _product == None:
            return Response(status="Error",
                            code="404",
                            message="Product not found").dict(exclude_none=True)

        elif has_stock:
            message = "Quedan " + \
                str(_product.available_quantity) + " unidades en stock."
        else:
            message = "No hay suficientes "+_product.name_product

        return Response(status="OK",
                        code="200",
                        message=message).dict(exclude_none=True)
