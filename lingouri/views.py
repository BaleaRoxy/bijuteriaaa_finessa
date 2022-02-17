from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from lingouri.models import Produse
from utils.cart.cart import Cart


def show_all_lingouri(request):
    lingouri = Produse.objects.all().order_by("id")
    paginator = Paginator(lingouri, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'lingouri/lingouri.html', {
        'page_obj': page_obj,
        'cart_lingouri': len(request.session['cart'].keys())
    })


def show_lingou_details(request, lingou_id):
    lingou = get_object_or_404(Produse, pk=lingou_id)

    return render(request, 'lingouri/details.html', {
        'lingou': lingou,
    })


def add_lingou_to_cart(request, lingou_id):
    lingou = get_object_or_404(Produse, id=lingou_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(lingou_id, quantity)


    return redirect(reverse('lingouri:all'))
