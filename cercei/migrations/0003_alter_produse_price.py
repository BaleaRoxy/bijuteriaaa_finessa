# Generated by Django 3.2.9 on 2022-02-16 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cercei', '0002_produse_sistem_inchidere'),
    ]

    operations = [
        migrations.AlterField(
            model_name='produse',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]