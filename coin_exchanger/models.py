from django.db import models

# Create your models here.
class ExchangeOrder(models.Model):
    order_id = models.AutoField(primary_key=True)
    send_coin_type = models.CharField(max_length=10)
    recv_coin_type = models.CharField(max_length=10)

    recv_address = models.CharField(max_length=200)
    refund_address = models.CharField(max_length=200)