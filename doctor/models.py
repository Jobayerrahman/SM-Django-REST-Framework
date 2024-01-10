from django.db import models

# Create your models here.

class Doctor(models.Model):
    doctor_name         = models.CharField(max_length=60)
    doctor_speciality   = models.CharField(max_length=60)
    doctor_schedule     = models.TimeField()
    doctor_visit         = models.IntegerField()
