from fastapi import APIRouter
from pydantic import BaseModel
from db.config import SessionLocal
import db.crud as crud
from db.schemas import Request, Response
from sqlalchemy.orm import Session
from fastapi import Depends
from typing import List

router = APIRouter()


@router.post("/image")
async def set_image():
    return {"message": "Hello World"}
