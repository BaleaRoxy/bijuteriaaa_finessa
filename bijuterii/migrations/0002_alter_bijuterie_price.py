# Generated by Django 3.2.9 on 2022-02-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bijuterii', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bijuterie',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=8),
        ),
    ]
