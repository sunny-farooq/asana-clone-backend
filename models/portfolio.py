from tortoise.models import Model
from tortoise import fields

class portfolio(Model):
    id = fields.UUIDField(pk=True)
    organization = fields.ForeignKeyField("models.organization", related_name='Organization Portfolio', on_delete=fields.OnDelete.CASCADE )
    owner = fields.ForeignKeyField("models.account", related_name='Portfolio Owner', on_delete=fields.OnDelete.CASCADE )
    name = fields.CharField(max_length=20)
    status = fields.CharField(max_length = 10, null=True)
    start_date = fields.DateField(null=True)
    end_date = fields.DateField(null=True)
    isOngoing = fields.BooleanField(default=False)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Portfolios"