from fastapi import FastAPI
from private_api.app.routers.routers_meme import router

app = FastAPI()

app.include_router(router)
