import json
from users.models.details import Cart as CartModel
from bijuterii.models import Bijuterie
# from payments.models import Order, OrderItem


class Cart:
    def __init__(self, request):
        self._user = request.user
        self._data = request.session['cart'] if 'cart' in request.session else {}
        self._session = request.session

    @property
    def amount(self):
        bijuterii = Bijuterie.objects.filter(id__in=self._data.keys())
        return self._get_bijuterii_total(bijuterii)

    def _get_bijuterii_total(self, bijuterii):
        total = sum([
            float(bijuterie.price) * int(self._data[str(bijuterie.id)])
            for bijuterie in bijuterii
        ])

        return total

    def add(self, bijuterie_id, quantity):
        bijuterie_id_str = str(bijuterie_id)

        if bijuterie_id_str in self._data:  # { '4': '10' }
            old_quantity = self._data[bijuterie_id_str]
            old_quantity = int(old_quantity)

            new_quantity = old_quantity + quantity

            self._data[bijuterie_id_str] = str(new_quantity)
        else:
            self._data[bijuterie_id_str] = str(quantity)

        self._save()

    def remove(self, bijuterie_id):
        del self._data[str(bijuterie_id)]
        self._save()

    def _save(self):
        self._session['cart'] = self._data

        if hasattr(self._user, 'cart'):
            self._user.cart.data = json.dumps(self._data)
            self._user.cart.save()
        else:
            CartModel.objects.create(user=self._user, data=json.dumps(self._data))

    # def create_order(self):
    #     order = Order.objects.create(
    #         user=self._user,
    #     )
    #
    #     bijuterii = bijuterie.objects.filter(id__in=self._data.keys())
    #     total = self._get_bijuterii_total(bijuterii)
    #
    #     for bijuterie in bijuterii:
    #         OrderItem.objects.create(
    #             order=order,
    #             bijuterie=bijuterie,
    #             price=bijuterie.price,
    #         )
    #
    #     self._reset()
    #
    #     return order, total
    #
    # def _reset(self):
    #     self._data = {}
    #     self._save()

