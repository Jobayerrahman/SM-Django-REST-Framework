from django.db import models

# Create your models here.

class Invoice(models.Model):
    customer_name           = models.CharField(max_length=40)
    customer_contact        = models.CharField(max_length=60)
    number_of_items         = models.IntegerField()
    invoice_date            = models.DateField()
