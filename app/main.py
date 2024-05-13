from fastapi import FastAPI
from router.supply_request_router import router as api_router
import app.inventory.db.model as model
from app.inventory.db.config import engine
from app.mq_supply import consumer_supply


model.Base.metadata.create_all(bind=engine)


def get_application() -> FastAPI:
    application = FastAPI(title="PROJECT_NAME",
                          debug="DEBUG", version="VERSION")

    application.include_router(api_router, prefix="/api/v1")

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
