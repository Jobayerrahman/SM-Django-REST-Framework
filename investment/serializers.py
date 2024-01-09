from rest_framework import serializers
from .models import Investment

class InvestmentSerializer(serializers.ModelSerializer):
    class Meta:
        model   = Investment
        fields  =['investment_code','investor_name','investor_contact','investment_amount']