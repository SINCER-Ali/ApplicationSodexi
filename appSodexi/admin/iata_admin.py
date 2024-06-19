from django.contrib import admin
from ..models import Iata
#deux ligne obligatoire convention


@admin.register(Iata)
class IataAdmin(admin.ModelAdmin):
    list_display = ['iata_pays', 'iata_escale', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']



