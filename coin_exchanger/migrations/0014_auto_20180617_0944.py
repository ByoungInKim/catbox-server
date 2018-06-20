# Generated by Django 2.0.6 on 2018-06-17 09:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_exchanger', '0013_auto_20180617_0936'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiondetailinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='transaction',
            name='details',
            field=models.ManyToManyField(to='coin_exchanger.TransactionDetailInfo'),
        ),
        migrations.AddField(
            model_name='transactiondetailinfo',
            name='detail_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]