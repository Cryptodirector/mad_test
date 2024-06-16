import uvicorn
from fastapi import FastAPI
from public_api.app.routers.meme_routers import router as public


app = FastAPI()

app.include_router(public)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)