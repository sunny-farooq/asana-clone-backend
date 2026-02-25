from tortoise.models import Model
from tortoise import fields

class project(Model):
    id = fields.UUIDField(pk=True)
    portfolio=fields.ForeignKeyField("models.portfolio",related_name="portfolio associated", on_delete=fields.OnDelete.CASCADE, null=True )
    organization = fields.ForeignKeyField('models.organization', related_name="Organization Asscociated for project", on_delete=fields.OnDelete.CASCADE)
    name = fields.CharField(max_length=40)
    status = fields.CharField(max_length=30)
    created_at = fields.DatetimeField(auto_now_add=True)  
    updated_at = fields.DatetimeField(auto_now=True)

    class Meta:
        table = "Projects"