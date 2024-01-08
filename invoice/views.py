from django.shortcuts import render
from .models import Invoice
from .serializers import InvoiceSerializer
from rest_framework.views import APIView
from rest_framework.response import Response


class Invoice_view(APIView):
    def get(self, request, pk=None, formate=None):
        invoice_id = pk
        if invoice_id is not None:
            invoice     = Invoice.objects.get(id=invoice_id)
            serializer  = InvoiceSerializer(invoice)
            return Response(serializer.data)
        invoices    = Invoice.objects.all()
        serializer  = InvoiceSerializer(invoices,many=True)
        return Response(serializer.data)
    def post(self, request, pk=None, formate=None):
        serializer = InvoiceSerializer(data= request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message' : 'Invoice data save successfully'})
        return Response({'message': serializer.errors})
            
    def put(self, request, pk, formate=None):
        invoice_id = pk
        invoice    = Invoice.objects.get(pk=invoice_id)
        serializer = InvoiceSerializer(invoice, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Invoice data update successfully'})
        return Response({'message': serializer.errors})
    def patch(self, request, pk, formate=None):
        invoice_id = pk
        invoice    = Invoice.objects.get(pk=invoice_id)
        serializer = InvoiceSerializer(invoice,data=request.data,partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Invoice data partial update successfully'})
        return Response({'message': serializer.errors})
    def delete(self, request, pk, formate=None):
        invoice_id = pk
        invoice = Invoice.objects.get(pk=invoice_id)
        invoice.delete()
        return Response({'message':'Invoice data successfully'})
