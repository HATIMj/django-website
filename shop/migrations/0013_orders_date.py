# Generated by Django 4.0.1 on 2022-04-08 17:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0012_alter_orders_zip_code'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='date',
            field=models.DateField(default=datetime.datetime(2022, 4, 8, 17, 28, 31, 49824)),
        ),
    ]
