# Generated by Django 2.0.6 on 2018-06-17 09:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coin_exchanger', '0006_transaction_detail'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='detail',
            new_name='details',
        ),
    ]
