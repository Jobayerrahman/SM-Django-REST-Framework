from django.db import models

# Create your models here.

class Inventory(models.Model):
    product_code    = models.CharField(max_length=60)
    product_name    = models.CharField(max_length=60)
    product_amount  = models.CharField(max_length=50)
    product_entry   = models.DateField()
    product_expiry  = models.DateField()