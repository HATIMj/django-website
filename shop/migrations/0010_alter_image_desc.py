# Generated by Django 4.0.1 on 2022-04-05 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_image_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.TextField(default='o', max_length=200),
        ),
    ]
