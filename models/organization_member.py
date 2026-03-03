from tortoise.models import Model
from tortoise import fields
from enum import Enum

class UserRole(str, Enum):
    ADMIN = "admin"
    USER = "user"

class organization_member(Model):
    id = fields.UUIDField(pk = True)
    organization = fields.ForeignKeyField('models.organization', related_name="Organization", on_delete=fields.OnDelete.CASCADE, null=True)
    account = fields.ForeignKeyField('models.account', related_name='Organization Member', on_delete=fields.OnDelete.CASCADE, null = True)
    email = fields.CharField(max_length=40, unique=True, null = True)
    role = fields.CharEnumField(UserRole, default=UserRole.USER)
    invitation_code = fields.CharField(max_length=6, null= True)
    joined_at= fields.DatetimeField(auto_now_add=True)
    invited_at = fields.DatetimeField(null = True)

    class Meta:
        table = "Organization_Members"