from tortoise.models import Model
from tortoise import fields

class goal_tasks(Model):
    id = fields.UUIDField(pk = True)
    goal = fields.ForeignKeyField("models.goal", related_name="Goals associated with tickets", on_delete=fields.OnDelete.CASCADE)
    task = fields.ForeignKeyField("models.task", related_name="goals and tasms", on_delete=fields.OnDelete.CASCADE)

    class Meta:
        table = "Goal_Tasks"


