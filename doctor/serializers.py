from rest_framework import serializers
from .models import Doctor

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Doctor
        fields  = ['doctor_name','doctor_speciality','doctor_schedule','doctor_visit']