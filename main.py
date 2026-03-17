from fastapi import FastAPI
from controllers import user_controller
from controllers import organization_controller
from controllers import project_controller
from controllers import task_controller
from controllers import comment_controller
from controllers import portfolio_controller, goal_controller
from controllers import org_worker
from contextlib import asynccontextmanager
from tortoise import Tortoise
from helpers.tortoise_config import TORTOISE_CONFIG
from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost",
    "http://localhost:8080",
    "http://localhost:5173"
]


# async def lifespan(app: FastAPI):
#     await init()
#     print("Starting DB")

#     yield
#     print("Closing")


@asynccontextmanager
async def lifespan(app):
    await Tortoise.init(
      config=TORTOISE_CONFIG,
    )
    print("Starting DB")

    # await Tortoise.generate_schemas()
    yield
    print("Closing DB")
    await Tortoise.close_connections()

app = FastAPI(lifespan=lifespan)

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(router = user_controller.user_router)
app.include_router(router=organization_controller.organization_router)
app.include_router(router=project_controller.project_router)
app.include_router(router=task_controller.task_router)
app.include_router(router=comment_controller.comment_router)
app.include_router(router=portfolio_controller.portfolio_router)
app.include_router(router=goal_controller.goal_router)
app.include_router(router=org_worker.org_worker)