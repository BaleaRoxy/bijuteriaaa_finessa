# Generated by Django 3.2.9 on 2022-02-16 13:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pandative', '0004_alter_produse_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='produse',
            name='stone_color',
        ),
    ]
