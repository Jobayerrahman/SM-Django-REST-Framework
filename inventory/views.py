from django.shortcuts import render
from .models import Inventory
from .serializers import InventorySerializer
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin

class inventoryList(GenericAPIView,ListModelMixin):
    queryset          = Inventory.objects.all()
    serializer_class  = InventorySerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

class inventoryCreate(GenericAPIView, CreateModelMixin):
    queryset           = Inventory.objects.all()
    serializer_class   = InventorySerializer

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

class inventoryRetrieve(GenericAPIView,RetrieveModelMixin):
    queryset           = Inventory.objects.all()
    serializer_class   = InventorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

class inventoryUpdate(GenericAPIView,RetrieveModelMixin,UpdateModelMixin):
    queryset           = Inventory.objects.all()
    serializer_class   = InventorySerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
        
class inventoryDestroy(GenericAPIView,DestroyModelMixin):
    queryset           = Inventory.objects.all()
    serializer_class   = InventorySerializer

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
