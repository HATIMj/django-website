# Generated by Django 4.0.1 on 2022-05-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0024_orders'),
    ]

    operations = [
        migrations.AddField(
            model_name='orders',
            name='items',
            field=models.CharField(default=None, max_length=555),
        ),
    ]
