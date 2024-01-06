from rest_framework import serializers
from .models import Product

class ProductSerializer(serializers.Serializer):
    product_name    = serializers.CharField(max_length=30)
    group_name      = serializers.CharField(max_length=30)
    product_price   = serializers.CharField(max_length=30)
    product_amount  = serializers.IntegerField()

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.product_name   = validated_data.get('product_name',instance.product_name)
        instance.group_name     = validated_data.get('group_name',instance.group_name)
        instance.product_price  = validated_data.get('product_price',instance.product_price)
        instance.product_amount = validated_data.get('product_amount',instance.product_amount)
        instance.save()
        return instance

    