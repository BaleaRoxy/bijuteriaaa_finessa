# Generated by Django 3.2.9 on 2022-02-16 13:05

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_activation_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 16, 13, 35, 59, 320556, tzinfo=utc)),
        ),
    ]
