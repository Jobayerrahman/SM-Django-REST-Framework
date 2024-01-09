from django.shortcuts import render
from .models import Customer
from .serializers import CustomerSerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, RetrieveModelMixin, CreateModelMixin, UpdateModelMixin, DestroyModelMixin


class Customer_list_create(GenericAPIView,ListModelMixin):
    queryset            = Customer.objects.all()
    serializer_class    = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class Customer_retrieve_update_destroy(GenericAPIView,RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin):
    queryset            = Customer.objects.all()
    serializer_class    = CustomerSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destory(request, *args, **kwargs)



