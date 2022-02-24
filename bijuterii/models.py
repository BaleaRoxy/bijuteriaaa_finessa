from django.db import models

from django.contrib.auth import get_user_model

AuthUserModel = get_user_model()

class Culoareaur(models.Model):
    name = models.CharField(max_length=128, null=False)

class Bijuterie(models.Model):
    name = models.CharField(max_length=128, null=False)
    # producty_type = models.CharField(max_length= 15, null=False)
    # product = models.ForeignKey(Bijuterie, on_delete=models.CASCADE)
    culoriaur = models.ManyToManyField(Culoareaur, through='BijuterieCuloareaur')
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2) # minȘ 0.00
    color_gold = models.CharField(max_length=10, null=False)
    greutate = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.IntegerField( default=0 , null=False )
    # image = models.ImageField

    def __str__(self):
        return f'<Bijuterie object ID = {self.name}>'

class BijuterieCuloareaur(models.Model):
    bijuterie = models.ForeignKey(Bijuterie, on_delete=models.CASCADE, related_name='categories_pivot')  # product.categories[0].category.name
    culoareaur = models.ForeignKey(Culoareaur, on_delete=models.CASCADE, related_name='bijuterii_pivot')  # category.products[0].product.name
    extra_column = models.IntegerField(null=True, default=None)