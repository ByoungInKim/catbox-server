from rest_framework import routers
from coin_exchanger.viewsets import ExchangeOrderViewSet, TransactionViewSet
router = routers.DefaultRouter()

router.register(r'exchange_order', ExchangeOrderViewSet)
router.register(r'transaction', TransactionViewSet)