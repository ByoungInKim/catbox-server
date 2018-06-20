from rest_framework import viewsets, status
from .models import ExchangeOrder, Transaction
from .serializers import ExchangeOrderSerializer, TransactionSerializer
from rest_framework.response import Response
from coin_exchanger.coin.bitcoin_rpc import BitcoinRpc

class ExchangeOrderViewSet(viewsets.ModelViewSet):
    queryset = ExchangeOrder.objects.all()
    serializer_class = ExchangeOrderSerializer

    def create(self, request):
        bitcoin_rpc = BitcoinRpc()

        request_data = request.data
        send_address = str(bitcoin_rpc.get_new_address())
        min_amount = 0.001
        max_amount = bitcoin_rpc.get_balance() * 0.000000001

        request_data.update(send_address=send_address)
        request_data.update(min_amount=min_amount)
        request_data.update(max_amount=max_amount)

        serializer = ExchangeOrderSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class TransactionViewSet(viewsets.ModelViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer

    def create(self, request):
        request_data = request.data

        serializer = TransactionSerializer(data=request_data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
