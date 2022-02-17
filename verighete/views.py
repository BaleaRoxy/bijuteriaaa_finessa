from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from verighete.models import Produse
from utils.cart.cart import Cart


def show_all_verighete(request):
    verighete = Produse.objects.all().order_by("id")
    paginator = Paginator(verighete, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'verighete/verighete.html', {
        'page_obj': page_obj,
        'cart_verighete': len(request.session['cart'].keys())
    })


def show_modelverighete_details(request, modelverighete_id):
    modelverighete = get_object_or_404(Produse, pk=modelverighete_id)

    return render(request, 'verighete/details.html', {
        'modelverighete': modelverighete,
    })


def add_modelverighete_to_cart(request, modelverighete_id):
    modelverighete = get_object_or_404(Produse, id=modelverighete_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(modelverighete_id, quantity, 'verighete')


    return redirect(reverse('verighete:all'))
