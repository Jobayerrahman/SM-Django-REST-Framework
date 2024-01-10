from django.contrib import admin
from .models import Doctor

# Register your models here.

@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ['doctor_name','doctor_speciality','doctor_schedule','doctor_visit']
