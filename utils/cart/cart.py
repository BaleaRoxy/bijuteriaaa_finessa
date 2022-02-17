import json
from users.models.details import Cart as CartModel


class Cart:
    def __init__(self, request):
        self._user = request.user
        self._data = request.session['cart'] if 'cart' in request.session else {}
        self._session = request.session

    def add(self, model_id, quantity, product_type):
        model_id_str = str(model_id)

        if model_id_str in self._data[product_type]:  # { '4': '10' }
            old_quantity = self._data[model_id_str]
            old_quantity = int(old_quantity)

            new_quantity = old_quantity + quantity

            self._data[product_type][model_id_str] = str(new_quantity)
        else:
            self._data[model_id_str] = str(quantity)

        self._save()

    def remove(self, model_id):
        del self._data[str(model_id)]
        self._save()

    def _save(self):
        self._session['cart'] = self._data

        if hasattr(self._user, 'cart'):
            self._user.cart.data = json.dumps(self._data)
            self._user.cart.save()
        else:
            CartModel.objects.create(user=self._user, data=json.dumps(self._data))
# cart = {
#     'cercei': {'23': 2, '45': 1},
#     'bratari': {'2': 1},
# }
