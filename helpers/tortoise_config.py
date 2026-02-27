from tortoise import Tortoise
import os
from dotenv import load_dotenv
load_dotenv()

# async def init():
#     await Tortoise.init(
#         db_url = os.getenv("SUPABASE_DB"),
#         _enable_global_fallback=True,
#         modules = { "models" : ["models.organization","models.account","models.notification","models.portfolio", "models.goal","models.organization_member","models.project","models.task", "models.comment","models.task_like","models.goal_tasks","models.goal_projects" ] }
#     )
#     await Tortoise.generate_schemas()


# Config for aerich migrations - must be named TORTOISE_ORM
TORTOISE_ORM = {
    "connections": {
        "default": os.getenv("SUPABASE_DB"),
    },
    "apps": {
        "models": {
            "models": ["aerich.models","models.organization","models.account","models.notification","models.portfolio", "models.goal","models.organization_member","models.project","models.task", "models.comment","models.task_like","models.goal_tasks","models.goal_projects" ],
            "default_connection": "default",
        }
    }
}

# Alias for backwards compatibility
TORTOISE_CONFIG = TORTOISE_ORM
