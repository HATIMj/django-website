# Generated by Django 4.0.1 on 2022-03-31 13:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0008_alter_image_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='image',
            name='desc',
            field=models.TextField(default='', max_length=200),
        ),
    ]