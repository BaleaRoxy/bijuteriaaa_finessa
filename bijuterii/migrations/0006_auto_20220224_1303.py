# Generated by Django 3.2.9 on 2022-02-24 11:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bijuterii', '0005_bijuterieculoareaur_culoareaur'),
    ]

    operations = [
        migrations.RenameField(
            model_name='culoareaur',
            old_name='bijuterie',
            new_name='name',
        ),
        migrations.AddField(
            model_name='bijuterie',
            name='culoriaur',
            field=models.ManyToManyField(through='bijuterii.BijuterieCuloareaur', to='bijuterii.Culoareaur'),
        ),
    ]
