from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from cercei.models import Produse
from cercei.cart import Cart


def show_all_cercei(request):
    cercei = Produse.objects.all().order_by("id")
    paginator = Paginator(cercei, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'cercei/cercei.html', {
        'page_obj': page_obj,
        'cart_cercei': len(request.session['cart'].keys())
    })


def show_modelcercei_details(request, modelcercei_id):
    modelcercei = get_object_or_404(Produse, pk=modelcercei_id)

    return render(request, 'cercei/details.html', {
        'modelcercei': modelcercei,
    })


def add_modelcercei_to_cart(request, modelcercei_id):
    modelcercei = get_object_or_404(Produse, id=modelcercei_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(modelcercei_id, quantity, 'cercei')



    return redirect(reverse('cercei:all'))
