from django.shortcuts import render
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer


@api_view(['GET','POST','PUT','PATCH','DELETE'])
def employee_view(request, pk=None):
    if request.method == 'GET':
        employee_id = pk
        if employee_id is not None:
            employees   = Employee.objects.get(id=employee_id)
            serializer  = EmployeeSerializer(employees)
            return Response(serializer.data)
        employees  = Employee.objects.all()
        serializer = EmployeeSerializer(employees,many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Employee data save successfully'})
        return Response(serializer.errors)
    
    if request.method == 'PUT':
        employee_id = pk
        employee    = Employee.objects.get(pk=employee_id)
        serializer  = EmployeeSerializer(employee,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Employee data update successfully'})
        return Response({'message': serializer.errors})

    if request.method == 'PATCH':
        employee_id = pk
        employee    = Employee.objects.get(pk=employee_id)
        serializer  = EmployeeSerializer(employee,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Employee partial data update successfully'})
        return Response({'message': serializer.errors})

    if request.method == 'DELETE':
        employee_id     = pk
        employee        = Employee.objects.get(pk=employee_id)
        employee.delete()
        return Response({'message':'Employee data deleted successfully'})
