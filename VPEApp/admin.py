
# Register your models here.
from django.contrib import admin
from .models import EvaluationType, UsersList

@admin.register(EvaluationType)
class EvaluationTypeAdmin(admin.ModelAdmin):
    list_display = ['Id', 'EvaluationType', 'DeliveryPercent', 'PriceChangesPercent', 'QualityPercent', 'ServicePercent']

@admin.register(UsersList)
class UsersListAdmin(admin.ModelAdmin):
    list_display = ['Id', 'GlobalId', 'Name']
