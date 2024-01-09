from django.shortcuts import render
from .models import Investment
from .serializers import InvestmentSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

class Investment_list_create(ListCreateAPIView):
    queryset            = Investment.objects.all()
    serializer_class    = InvestmentSerializer

class Investment_retrieve_update_destroy(RetrieveUpdateDestroyAPIView):
    queryset            = Investment.objects.all()
    serializer_class    = InvestmentSerializer
