from django import template
from bijuterii.models import Bijuterie

register = template.Library()


# @register.filter(name='products_no')
# def get_cart_products_number(session):
#     cart = session.get('cart', {})
#     return len(cart.keys())


# @register.filter(name='dict_length')
# def dict_length(parent, key):
#     my_dict = parent.get(key, {})
#     dictlength = 0
#     for key in my_dict.keys():
#         dictlength += len(my_dict[key])
#     return dictlength
@register.filter(name='dict_length')
def dict_length(parent, key):
    my_dict = parent.get(key, {})
    return len(my_dict.keys())

@register.simple_tag(name='cart_data')
def get_cart_data(parent, key):
    my_dict = parent.get(key, {})
    return {
        'items': len(my_dict.keys()),
        'total': '%.2f' % 250.55
    }


@register.inclusion_tag(filename='bijuterii/tags/cart.html', name='cart_link')
def get_cart_link(session):
    cart = session.get('cart', {})
    bijuterie_ids = cart.keys()

    print('cart', cart)
    bijuterii = Bijuterie.objects.filter(id__in=bijuterie_ids)
    print('cart.values()', list(cart.values()))

    total = sum(
        [
            float(bijuterie.price) * int(cart[str(bijuterie.id)])
            for bijuterie in bijuterii
        ]
    )  # sum([49.90 * 1, 24.90 * 1]) => sum([49.90, 24.90])

    return {
        'items': len(bijuterie_ids),
        'total': '%.2f' % total
    }