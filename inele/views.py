from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from inele.models import Produse
from utils.cart.cart import Cart


def show_all_inele(request):
    inele = Produse.objects.all().order_by("id")
    paginator = Paginator(inele, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'inele/inele.html', {
        'page_obj': page_obj,
        'cart_inele': len(request.session['cart'].keys())
    })


def show_inel_details(request, inel_id):
    inel = get_object_or_404(Produse, pk=inel_id)

    return render(request, 'inele/details.html', {
        'inel': inel,
    })


def add_inel_to_cart(request, inel_id):
    inel = get_object_or_404(Produse, id=inel_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(inel_id, quantity)


    return redirect(reverse('inele:all'))
