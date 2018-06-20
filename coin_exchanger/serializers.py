from rest_framework import serializers
from .models import ExchangeOrder, Transaction, TransactionDetailInfo

class TransactionDetailInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = TransactionDetailInfo
        fields = '__all__'

class TransactionSerializer(serializers.ModelSerializer):
    details = TransactionDetailInfoSerializer(many=True)

    class Meta:
        model = Transaction
        fields = '__all__'
        depth = 1
    
    def create(self, validated_data):
        details_data = validated_data.pop('details')
        transaction = Transaction.objects.create(**validated_data)

        for detail in details_data:
            # todo - change parameter
            detail_info = TransactionDetailInfo.objects.create(
                account = detail['account'],
                address = detail['address'],
                category = detail['category'],
                amount = detail['amount'],
                label = detail['label'],
                vout = detail['vout']
            )
            transaction.details.add(detail_info)
        return transaction

class ExchangeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeOrder
        fields = '__all__'
        depth = 2

