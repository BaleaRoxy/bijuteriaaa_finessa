# Generated by Django 3.2.9 on 2022-02-18 12:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0016_alter_activation_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activation',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2022, 2, 18, 12, 42, 56, 223467, tzinfo=utc)),
        ),
    ]