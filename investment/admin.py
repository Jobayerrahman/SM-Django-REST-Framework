from django.contrib import admin
from .models import Investment
# Register your models here.

@admin.register(Investment)
class InvestmentAdmin(admin.ModelAdmin):
    list_display=['investment_code','investor_name','investor_contact','investment_amount']
