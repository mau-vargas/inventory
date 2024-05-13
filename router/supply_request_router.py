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
    name: str
    category: str
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
        return crud.product_request(db, product)
