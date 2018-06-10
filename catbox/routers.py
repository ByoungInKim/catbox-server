from rest_framework import routers
from coin_exchanger.viewsets import ExchangeOrderViewSet
router = routers.DefaultRouter()
router.register(r'exchange_order', ExchangeOrderViewSet)