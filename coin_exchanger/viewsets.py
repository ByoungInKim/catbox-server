from rest_framework import viewsets, status
from .models import ExchangeOrder
from .serializers import ExchangeOrderSerializer
from rest_framework.response import Response
from coin_exchanger.coin.bitcoin_rpc import BitcoinRpc

class ExchangeOrderViewSet(viewsets.ModelViewSet):
    queryset = ExchangeOrder.objects.all()
    serializer_class = ExchangeOrderSerializer

    def create(self, request):
        request_data = request.data
        send_address = str(BitcoinRpc().get_new_address())
        request_data.update(send_address=send_address)

        serializer = ExchangeOrderSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
