# Generated by Django 2.0.6 on 2018-06-17 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_exchanger', '0009_auto_20180617_0929'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='transactiondetailinfo',
            name='id',
        ),
        migrations.AddField(
            model_name='transactiondetailinfo',
            name='detail_id',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
            preserve_default=False,
        ),
    ]
