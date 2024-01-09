from django.db import models

# Create your models here.

class Investment(models.Model):
    investment_code         = models.CharField(max_length=60)
    investor_name           = models.CharField(max_length=60)
    investor_contact        = models.CharField(max_length=80)
    investment_amount       = models.CharField(max_length=60)
