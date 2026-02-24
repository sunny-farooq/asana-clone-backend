from tortoise.models import Model
from tortoise import fields

class goal(Model):
    id = fields.UUIDField(pk=True)
    owner_id = fields.ForeignKeyField('models.account', related_name='goals', on_delete=fields.OnDelete.CASCADE)
    organization_id = fields.ForeignKeyField('models.organization', related_name="Organization Goals", on_delete=fields.OnDelete.CASCADE),
    title=fields.CharField(max_length=20)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Goals"