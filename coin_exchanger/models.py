from django.db import models

class TransactionDetailInfo(models.Model):
    #detail_id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)
    category = models.CharField(max_length=20)
    amount = models.FloatField(default=0)
    label = models.CharField(max_length=500, blank=True)
    vout = models.IntegerField(default=0, blank=True)
    fee = models.FloatField(default=0, blank=True)
    abandoned = models.NullBooleanField(null=True, blank=True)

class Transaction(models.Model):
    txid = models.CharField(primary_key=True, max_length=200)
    confirmations = models.IntegerField(default=0)
    amount = models.FloatField(default=0)
    
    blockhash = models.CharField(max_length=200, default=None)
    blockindex = models.IntegerField(default=0)
    blocktime = models.IntegerField(default=0)

    time = models.IntegerField(default=0)
    timereceived = models.IntegerField(default=0)

    hex = models.CharField(max_length=500)

    details = models.ManyToManyField(TransactionDetailInfo)

    # only for send transaction 
    fee = models.FloatField(default=0, blank=True)

class ExchangeOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    send_coin_type = models.CharField(max_length=10)
    recv_coin_type = models.CharField(max_length=10)

    recv_address = models.CharField(max_length=200)
    refund_address = models.CharField(max_length=200)

    # generate from server
    send_address = models.CharField(max_length=200, default=None, blank=True)
    
    min_amount = models.FloatField(default=0, blank=True)
    max_amount = models.FloatField(default=0, blank=True)

    transaction_list = models.ManyToManyField(Transaction)

