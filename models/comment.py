from tortoise.models import Model
from tortoise import fields

class comment(Model):
    id = fields.UUIDField(pk=True)
    task=fields.ForeignKeyField("models.task", related_name="task on which the comment was made", on_delete=fields.OnDelete.CASCADE)
    account = fields.ForeignKeyField("models.account", related_name="Person to whom task was assigned to", on_delete=fields.OnDelete.CASCADE)
    comment_text = fields.CharField(max_length=1000)
    has_attachment=fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Comments"
