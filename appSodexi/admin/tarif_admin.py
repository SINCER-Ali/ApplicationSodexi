from django.contrib import admin
from ..models import Tarif


@admin.register(Tarif)
class TarifAdmin(admin.ModelAdmin):
    list_display = ['origine', 'destination', 'minimum', 'convention', 'created_at', 'updated_at']
    readonly_fields = ['created_at', 'updated_at']


