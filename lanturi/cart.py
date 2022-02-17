import json
from users.models.details import Cart as CartModel
from lanturi.cart import Cart


class Cart:
    def __init__(self, request):
        self._user = request.user
        self._data = request.session['cart'] if 'cart' in request.session else {}
        self._session = request.session

    def add(self, lant_id, quantity):
        lant_id_str = str(lant_id)

        if lant_id_str in self._data:  # { '4': '10' }
            old_quantity = self._data[lant_id_str]
            old_quantity = int(old_quantity)

            new_quantity = old_quantity + quantity

            self._data[lant_id_str] = str(new_quantity)
        else:
            self._data[lant_id_str] = str(quantity)

        self._save()

    def remove(self, lant_id):
        del self._data[str(lant_id)]
        self._save()

    def _save(self):
        self._session['cart'] = self._data

        if hasattr(self._user, 'cart'):
            self._user.cart.data = json.dumps(self._data)
            self._user.cart.save()
        else:
            CartModel.objects.create(user=self._user, data=json.dumps(self._data))
