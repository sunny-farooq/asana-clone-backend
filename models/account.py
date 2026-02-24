from tortoise.models import Model
from tortoise import fields

class account(Model):
    id = fields.UUIDField(pk=True)
    organization_id = fields.ForeignKeyField('models.organization',  related_name='projects', on_delete=fields.OnDelete.CASCADE)
    email = fields.CharField(max_length=40, unique=True)
    name=fields.CharField(max_length=40)
    password = fields.CharField(max_length=50)
    is_verified = fields.BooleanField(default = False)
    role = fields.CharField(max_length=10)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Accounts"

