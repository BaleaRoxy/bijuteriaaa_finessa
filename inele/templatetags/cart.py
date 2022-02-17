from django import template
from cercei.models import Produse

register = template.Library()




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


@register.inclusion_tag(filename='inele/tags/cart.html', name='cart_link')
def get_cart_link(session):
    cart = session.get('cart', {})
    inel_ids = cart.keys()

    print('cart', cart)
    inele = Produse.objects.filter(id__in=inel_ids)
    print('cart.values()', list(cart.values()))

    total = sum(
        [
            float(inel.price) * int(cart[str(inel.id)])
            for inel in inele
        ]
    )  # sum([49.90 * 1, 24.90 * 1]) => sum([49.90, 24.90])

    return {
        'items': len(inel_ids),
        'total': '%.2f' % total
    }