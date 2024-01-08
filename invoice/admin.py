from django.contrib import admin
from .models import Invoice

# Register your models here.


@admin.register(Invoice)
class InvoiceAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name','customer_contact','number_of_items','invoice_date']
