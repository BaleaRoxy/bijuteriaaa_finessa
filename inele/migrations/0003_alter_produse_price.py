# Generated by Django 3.2.9 on 2022-02-16 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inele', '0002_auto_20211121_1923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produse',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]