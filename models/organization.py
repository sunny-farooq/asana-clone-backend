from tortoise.models import Model
from tortoise import fields

class organization(Model):
    id = fields.UUIDField(pk=True)
    name = fields.CharField(max_length=40, null = True)
    trial_status = fields.CharField(max_length=40, default = "Inactive")
    billing_date = fields.DateField(null = True)
    card_number = fields.CharField(max_length=12, null = True)
    card_expiry = fields.CharField(max_length=12, null = True)
    card_cvv = fields.CharField(max_length = 3,null = True)
    created_at = fields.DatetimeField(auto_now_add=True)
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Organizations"