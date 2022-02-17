from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from bratari.models import Bratara
from utils.cart.cart import Cart


def show_all_bratari(request):
    bratari = Bratara.objects.all().order_by("id")
    paginator = Paginator(bratari, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'bratari/bratari.html', {
        'page_obj': page_obj,
        'cart_bratari': len(request.session['cart'].keys())
    })


def show_bratara_details(request, bratara_id):
    bratara = get_object_or_404(Bratara, pk=bratara_id)

    return render(request, 'bratari/details.html', {
        'bratara': bratara,
    })


def add_bratara_to_cart(request, bratara_id):
    bratara = get_object_or_404(Bratara, id=bratara_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(bratara_id, quantity, 'bratari')


    return redirect(reverse('bratari:all'))