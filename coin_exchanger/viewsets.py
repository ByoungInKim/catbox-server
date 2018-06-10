from rest_framework import viewsets
from .models import ExchangeOrder
from .serializers import ExchangeOrderSerializer
class ExchangeOrderViewSet(viewsets.ModelViewSet):
    queryset = ExchangeOrder.objects.all()
    serializer_class = ExchangeOrderSerializer