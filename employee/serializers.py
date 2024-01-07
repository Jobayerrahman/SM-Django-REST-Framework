from rest_framework import serializers
from .models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields =['employee_name','employee_designation','employee_salary','employee_experiece']