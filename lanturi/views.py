from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from lanturi.models import Produse
from utils.cart.cart import Cart


def show_all_lanturi(request):
    lanturi = Produse.objects.all().order_by("id")
    paginator = Paginator(lanturi, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'lanturi/lanturi.html', {
        'page_obj': page_obj,
        'cart_lanturi': len(request.session['cart'].keys())
    })


def show_lant_details(request, lant_id):
    lant = get_object_or_404(Produse, pk=lant_id)

    return render(request, 'lanturi/details.html', {
        'lant': lant,
    })


def add_lant_to_cart(request, lant_id):
    lant = get_object_or_404(Produse, id=lant_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(lant_id, quantity)


    return redirect(reverse('lanturi:all'))