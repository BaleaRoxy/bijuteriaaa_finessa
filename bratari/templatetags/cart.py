from django import template
from bratari.models import Bratara

register = template.Library()


# @register.filter(name='products_no')
# def get_cart_products_number(session):
#     cart = session.get('cart', {})
#     return len(cart.keys())


@register.filter(name='dict_length')
def dict_length(parent, key):
    my_dict = parent.get(key, {})
    return len(my_dict.keys())


# @register.simple_tag(name='cart_data', takes_context=True)
# def get_cart_data(context, parent, key):
#     print(context['page_obj'], type(context['page_obj']))
#     my_dict = parent.get(key, {})
#     return len(my_dict.keys())

# @register.simple_tag(name='cart_data')
# def get_cart_data(parent, key):
#     my_dict = parent.get(key, {})
#     return len(my_dict.keys())

@register.simple_tag(name='cart_data')
def get_cart_data(parent, key):
    my_dict = parent.get(key, {})
    return {
        'items': len(my_dict.keys()),
        'total': '%.2f' % 250.55
    }


@register.inclusion_tag(filename='bratari/tags/cart.html', name='cart_link')
def get_cart_link(session):
    cart = session.get('cart', {})
    bratara_ids = cart.keys()

    print('cart', cart)
    bratari = Bratara.objects.filter(id__in=bratara_ids)
    print('cart.values()', list(cart.values()))

    total = sum(
        [
            float(bratara.price) * int(cart[str(bratara.id)])
            for bratara in bratari
        ]
    )  # sum([49.90 * 1, 24.90 * 1]) => sum([49.90, 24.90])

    return {
        'items': len(bratara_ids),
        'total': '%.2f' % total
    }