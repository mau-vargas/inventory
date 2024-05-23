from fastapi import APIRouter
from pydantic import BaseModel
from db.config import SessionLocal
import db.crud as crud
from db.schemas import Request, Response
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
    code: int | None = None
    name: str | None = None
    category: str | None = None
    count: int | None = None
    branch: str | None = None


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
            result_data = Product(
                description="Destornillador Phillips de 3/4 pulgada")

            return Response[Product](status="Error",
                                     code="404",
                                     message="Product not found", result=result_data)

        elif has_stock:
            message = "Quedan " + \
                str(_product.available_quantity) + " unidades en stock."
        else:
            message = "No hay suficientes "+_product.name_product

        result_data = Product()
        return Response(status="OK",
                        code="200",
                        message=message, result=result_data)
