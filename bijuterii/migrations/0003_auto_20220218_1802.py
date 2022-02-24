# Generated by Django 3.2.9 on 2022-02-18 16:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('bijuterii', '0002_alter_bijuterie_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bijuterie', models.CharField(max_length=128)),
            ],
        ),
        migrations.AddField(
            model_name='bijuterie',
            name='category',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bijuterii', to='bijuterii.category'),
        ),
    ]