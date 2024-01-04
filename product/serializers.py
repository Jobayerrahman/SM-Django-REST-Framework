from rest_framework import serializers

class ProductSerializer(serializers.Serializer):
    product_name    = serializers.CharField(max_length=30)
    group_name      = serializers.CharField(max_length=30)
    product_price   = serializers.CharField(max_length=30)
    product_amount  = serializers.IntegerField()