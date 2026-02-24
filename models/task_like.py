from tortoise.models import Model
from tortoise import fields

class task_like(Model):
    id = fields.UUIDField(pk=True)
    task = fields.ForeignKeyField("models.task", related_name="Like of the Task", on_delete=fields.OnDelete.CASCADE)
    account = fields.ForeignKeyField("models.account", related_name="Person who like the Task", on_delete=fields.OnDelete.CASCADE)
    created_at = fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "Task_Like"