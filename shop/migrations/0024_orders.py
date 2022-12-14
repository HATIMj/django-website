# Generated by Django 4.0.1 on 2022-05-18 16:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0023_delete_orders'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approved', models.BooleanField(default=False)),
                ('order_id', models.CharField(max_length=501)),
                ('name', models.CharField(max_length=120)),
                ('email', models.CharField(max_length=120)),
                ('address', models.CharField(max_length=120)),
                ('city', models.CharField(max_length=120)),
                ('state', models.CharField(max_length=120)),
                ('zip_code', models.CharField(max_length=120)),
            ],
        ),
    ]
