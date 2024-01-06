from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from .serializers import ProductSerializer
from .models import Product
from django.views.decorators.csrf import csrf_exempt
import io

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

def productCreate_view(request):
    if request.method == 'POST':
        json_data   = request.body
        stream_data = io.BytesIO(json_data)
        python_data = JSONParser().parse(stream_data)
        serializer  = ProductSerializer(data=python_data)
        if serializer.is_valid():
            serializer.save()
            response    = {'message':'Product created successfully'}
            json_data   = JSONRenderer().render(response) 
            return HttpResponse(json_data,content_type='application.json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application.json')
    
    if request.method == 'PUT':
        json_data       = request.body
        stream_data     = io.BytesIO(json_data)
        python_data     = JSONParser().parse(stream_data)
        product_id      = python_data.get(id)
        product_data    = Product.objects.get(id = product_id)
        serializer      = ProductSerializer(product_data,data=python_data,partial=True)
        if serializer.is_valid():
            serializer.save()
            response = {'message':'Product updated successfully'}
            json_data   = JSONRenderer().render(response) 
            return HttpResponse(json_data,content_type='application.json')
        else:
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data,content_type='application.json')

    if request.method == 'DELETE':
        json_data       = request.body
        stream_data     = io.BytesIO(json_data)
        python_data     = JSONParser().parse(stream_data)
        product_id      = python_data.get(id)
        product_data    = Product.objects.get(id = product_id)
        product_data.delete()
        response = {'message':'Product deleted successfully'}
        json_data   = JSONRenderer().render(response) 
        return HttpResponse(json_data,content_type='application.json')

