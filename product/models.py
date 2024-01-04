from django.db import models

# Create your models here.

class Product(models.Model):
    product_name    = models.CharField(max_length=30)
    group_name      = models.CharField(max_length=30)
    product_price   = models.CharField(max_length=30)
    product_amount  = models.IntegerField()
