# Generated by Django 2.0.6 on 2018-06-13 00:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coin_exchanger', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='exchangeorder',
            name='send_address',
            field=models.CharField(default='2018-06-13', max_length=200),
            preserve_default=False,
        ),
    ]
