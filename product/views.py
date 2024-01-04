from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from .serializers import ProductSerializer
from .models import Product

def productList_view(request):
    products    = Product.objects.all()
    serializer  = ProductSerializer(products, many=True)
    json_data   = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')


def product_view(request,pk):
    product     = Product.objects.get(id=pk)
    serializer  = ProductSerializer(product)
    json_data   = JSONRenderer().render(serializer.data)
    return HttpResponse(json_data, content_type='application/json')
