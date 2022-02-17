from django.db import models

# from django.contrib.auth import get_user_model
#
# AuthUserModel = get_user_model()


class Produse(models.Model):
    name = models.CharField(max_length=128, null=False)
    quantity = models.IntegerField(default=0, null=False)
    price = models.DecimalField(max_digits=8, decimal_places=2) # minȘ 0.00
    color_gold = models.CharField(max_length=10, null=False)
    greutate = models.DecimalField(max_digits=4, decimal_places=2)
    size = models.IntegerField( default=0 , null=False )
    inner_size = models.DecimalField(max_digits=5, decimal_places=2, null=True)
    stone_color = models.CharField(max_length=128, null=True)
    stone_type = models.CharField(max_length=128, null=True)


    def __str__(self):
        return f'<Product object ID = {self.id}>'