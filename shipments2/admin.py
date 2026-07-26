from django.contrib import admin
from .models import shipment

# Register your models here.
@admin.register(shipment)
class shipmentAdmin(admin.ModelAdmin):
    list_display = ('shipment_id', 'producto', 'FECHAETA', 'CANTIDAD', 'TOTAL', 'FECHADESPACHO', 'FECHAENTREGA')
    search_fields = ('producto', 'FECHAETA', 'NUMERODESPACHO')
    list_filter = ('FECHADESPACHO', 'FECHAENTREGA', 'VENCIMIENTO')
    ordering = ('shipment_id',)
    
