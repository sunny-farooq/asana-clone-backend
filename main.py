from fastapi import FastAPI
from helpers.tortoise_config import init
from controllers import user_controller
from controllers import organization_controller
from controllers import project_controller
from controllers import task_controller
from controllers import comment_controller
from controllers import portfolio_controller, goal_controller


async def lifespan(app: FastAPI):
    await init()
    print("Starting DB")

    yield
    print("Closing")

app = FastAPI(lifespan=lifespan)

app.include_router(router = user_controller.user_router)
app.include_router(router=organization_controller.organization_router)
app.include_router(router=project_controller.project_router)
app.include_router(router=task_controller.task_router)
app.include_router(router=comment_controller.comment_router)
app.include_router(router=portfolio_controller.portfolio_router)
app.include_router(router=goal_controller.goal_router)
