from django.db import models

# Create your models here.


class Customer(models.Model):
    customer_name       =models.CharField(max_length=60)
    customer_address    =models.CharField(max_length=60)
    customer_contact    =models.CharField(max_length=60)
    customer_due        =models.IntegerField()
