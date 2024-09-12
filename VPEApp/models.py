from django.db import models
import uuid

# Create your models here.

class EvaluationType(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    DeliveryPercent = models.IntegerField('Delivery Percent')
    EvaluationType = models.CharField('Description', max_length=50)
    PriceChangesPercent = models.IntegerField('Price Changes Percent')
    QualityPercent = models.IntegerField('Quality Percent')
    ServicePercent = models.IntegerField('Quality Percent')
    class Meta:
        db_table = "EvaluationType"

    def __str__(self):
        return self.EvaluationType
    
class UsersList(models.Model):
    Id = models.UUIDField(primary_key=True, default=uuid.uuid4, null=False)
    GlobalId = models.CharField('Global Id', max_length=50)
    Name = models.CharField('Name', max_length=500)

    class Meta:
        db_table = "Users"

    def __str__(self):
        return self.Name