from django.contrib import admin
from .models import ExchangeOrder, Transaction, TransactionDetailInfo

# Register your models here.
admin.site.register(ExchangeOrder)
admin.site.register(Transaction)
admin.site.register(TransactionDetailInfo)