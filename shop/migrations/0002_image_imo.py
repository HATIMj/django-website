# Generated by Django 4.0.1 on 2022-03-12 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='imo',
            field=models.ImageField(default=None, upload_to='images'),
        ),
    ]
