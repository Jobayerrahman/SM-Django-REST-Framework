from django.contrib import admin
from .models import Inventory
# Register your models here.

@admin.register(Inventory)
class InventoryAdmin(admin.ModelAdmin):
    list_display=['id','product_code','product_name','product_amount','product_entry','product_expiry']
