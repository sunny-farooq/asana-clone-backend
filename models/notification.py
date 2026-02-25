from tortoise.models import Model
from tortoise import fields

class notification(Model):
    id = fields.UUIDField(pk=True)
    recepient = fields.ForeignKeyField('models.account', related_name='notification', on_delete=fields.OnDelete.CASCADE )
    text = fields.CharField(max_length=30)
    created_at=fields.DatetimeField(auto_now_add=True)
    is_read=fields.BooleanField(default=False)

    class Meta:
        table = "Notifications"