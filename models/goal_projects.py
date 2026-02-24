from tortoise.models import Model
from tortoise import fields

class goal_projects(Model):
    id = fields.UUIDField(pk=True)
    goal = fields.ForeignKeyField("models.goal", related_name="project in the Goal", on_delete=fields.OnDelete.CASCADE)
    project = fields.ForeignKeyField("models.project", related_name="project in the goal mentioned", on_delete=fields.OnDelete.CASCADE)

    class Meta:
        table = "Goal Projects"