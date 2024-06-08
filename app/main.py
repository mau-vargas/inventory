from fastapi import FastAPI
from router.supply_request_router import router as api_router
from db import model
from db.config import engine
from mq_supply import consumer_supply
from router.fruit_router import router as fruit_router
from router.jwt_router import router as jwt_router

model.Base.metadata.create_all(bind=engine)

PREFIX = "/api/v1"
Version = "0.0.1"


def get_application() -> FastAPI:
    application = FastAPI(title="PROJECT_NAME",
                          debug="DEBUG", version=Version)

    application.include_router(api_router, prefix=PREFIX)
    application.include_router(fruit_router, prefix=PREFIX)
    application.include_router(jwt_router, prefix="")

    return application


app = get_application()


# app = FastAPI()


# @app.get("/")
# def read_root():
#     return {"Hello": "World"}


# @app.get("/inventory/show_products")
# async def show_products():
#     return {"test": "test"}


# @app.get("/items/{item_id}")
# def read_item(item_id: int, q: Union[str, None] = None):
#     return {"item_id": item_id, "q": q}
