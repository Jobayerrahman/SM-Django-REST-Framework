from django.db import models

# Create your models here.

class Employee(models.Model):
    employee_name           = models.CharField(max_length=60)
    employee_designation    = models.CharField(max_length=60)
    employee_salary         = models.CharField(max_length=30)
    employee_experiece      = models.IntegerField();
