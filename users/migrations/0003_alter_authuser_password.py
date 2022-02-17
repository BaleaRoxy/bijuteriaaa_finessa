
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_profile'),
    ]

    operations = [
        migrations.AlterField(
            model_name='authuser',
            name='password',
            field=models.CharField(default=None, max_length=128, null=True, verbose_name='password'),
        ),
    ]