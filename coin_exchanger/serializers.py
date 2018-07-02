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
            detail_info = TransactionDetailInfo.objects.create(**detail)
            transaction.details.add(detail_info)
        return transaction        
   
    def update(self, instance, validated_data):
        details_data = validated_data.pop('details')
        instance.blockhash = validated_data.get('blockhash', instance.blockhash)
        instance.save()

#        details = (instance.details).all()
 #       details = list(details)
  #      instance.Blockhash = 'aaa'
        #instance.last_name = validated_data.get('last_name', instance.last_name)
        #instance.instrument = validated_data.get('instrument', instance.instrument)
        
        #for detail in details_data:
        #    album = albums.pop(0)
        #    album.name = album_data.get('name', album.name)
        #    album.release_date = album_data.get('release_date', album.release_date)
        #    album.num_stars = album_data.get('num_stars', album.num_stars)
        #    album.save()
        #print(instance.Blockhash)
        return instance

class ExchangeOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ExchangeOrder
        fields = '__all__'
        depth = 2

