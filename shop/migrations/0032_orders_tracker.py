# Generated by Django 4.0.1 on 2022-11-02 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0031_alter_orders_items_alter_orders_order_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='Tracker',
            field=models.CharField(default='', max_length=50),
        ),
    ]
