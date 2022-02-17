from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from pandative.models import Produse
from utils.cart.cart import Cart


def show_all_pandative(request):
    pandative = Produse.objects.all().order_by("id")
    paginator = Paginator(pandative, 10)

    page_obj = paginator.get_page(request.GET.get('page'))

    return render(request, 'pandative/pandative.html', {
        'page_obj': page_obj,
        'cart_pandative': len(request.session['cart'].keys())
    })


def show_pandativ_details(request, pandativ_id):
    pandativ = get_object_or_404(Produse, pk=pandativ_id)

    return render(request, 'pandative/details.html', {
        'pandativ': pandativ,
    })


def add_pandativ_to_cart(request, pandativ_id):
    pandativ = get_object_or_404(Produse, id=pandativ_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(pandativ_id, quantity)


    return redirect(reverse('pandative:all'))
