from rest_framework import serializers
from .models import ExchangeOrder
class ExchangeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeOrder
        fields = '__all__'