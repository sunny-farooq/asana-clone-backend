from tortoise.models import Model
from tortoise import fields

class task(Model):
    id = fields.UUIDField(pk=True)
    project = fields.ForeignKeyField("models.project", related_name="Task assciated with project", on_delete=fields.OnDelete.CASCADE)
    category = fields.CharField(max_length=20)
    assignee = fields.ForeignKeyField("models.account", related_name="Person Assigned to", on_delete=fields.OnDelete.CASCADE)
    assign_date = fields.DateField()
    due_date = fields.DateField()
    priority = fields.CharField(max_length=20)
    status = fields.CharField(max_length=20)
    parent_task_id=fields.CharField(max_length=100)
    is_subtask= fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Tasks"