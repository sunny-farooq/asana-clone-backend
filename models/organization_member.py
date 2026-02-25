from tortoise.models import Model
from tortoise import fields

class organization_member(Model):
    id = fields.UUIDField(pk = True)
    organization = fields.ForeignKeyField('models.organization', related_name="Organization", on_delete=fields.OnDelete.CASCADE)
    account_id = fields.ForeignKeyField('models.account', related_name='Organization Member', on_delete=fields.OnDelete.CASCADE)
    role = fields.CharField(max_length=40)
    joined_at= fields.DatetimeField(auto_now_add=True)

    class Meta:
        table = "Organization_Members"