# Generated by Django 3.1.5 on 2021-09-03 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0009_auto_20210903_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='summary',
            field=models.TextField(blank=True, null=True),
        ),
    ]
