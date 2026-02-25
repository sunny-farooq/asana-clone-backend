from fastapi import FastAPI
from helpers.tortoise_config import init
from controllers import user_controller


async def lifespan(app: FastAPI):
    await init()
    print("Starting DB")

    yield
    print("Closing")

app = FastAPI(lifespan=lifespan)

app.include_router(router = user_controller.user_router)