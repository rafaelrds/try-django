# Generated by Django 2.0.7 on 2019-05-27 01:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(default='this is cool!'),
        ),
    ]
