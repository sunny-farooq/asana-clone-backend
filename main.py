from fastapi import FastAPI
from helpers.tortoise_config import init

async def lifespan(app: FastAPI):
    await init()
    print("Starting DB")

    yield
    print("Closing")

app = FastAPI(lifespan=lifespan)

@app.get("/")
def hello_world():
    return "Hello World"