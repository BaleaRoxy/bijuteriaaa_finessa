from django.shortcuts import render, get_object_or_404, Http404, redirect, reverse
from django.core.paginator import Paginator
from bijuterii.models import Bijuterie
from bijuterii.forms import FilterBijuterieForm, SelectCardForm
from utils.cart.cart import Cart


def show_all_bijuterii(request):
    print('request.GET', request.GET)
    form = FilterBijuterieForm(data=request.GET)
    bijuterii = form.apply_filters()

    paginator = Paginator(bijuterii, 4)
    page_obj = paginator.get_page(request.GET.get('page', 1))

    return render(request, 'bijuterii/bijuterii.html', {
        'page_obj': page_obj,
        # 'form': form,
        'form': FilterBijuterieForm()
    })


def show_bijuterie_details(request, bijuterie_id):

    bijuterie = get_object_or_404(Bijuterie, pk=bijuterie_id)

    return render(request, 'bijuterii/details.html', {
        'bijuterie': bijuterie,
    })


def add_bijuterie_to_cart(request, bijuterie_id):
    bijuterie = get_object_or_404(Bijuterie, id=bijuterie_id)
    quantity = request.POST.get('quantity')

    try:
        quantity = int(quantity)
    except (ValueError, TypeError):
        raise Http404('Quantity attribute is not valid.')

    cart = Cart(request)
    cart.add(bijuterie_id, quantity)

    return redirect(reverse('bijuterii:all'))


def show_checkout(request):
    cart = request.session.get('cart', {})
    bijuterii = Bijuterie.objects.filter(id__in=cart.keys())

    cart_items = [
        {
            "bijuterie": bijuterie,
            "quantity": cart[str(bijuterie.id)],
            "total": '%.2f' % (float(bijuterie.price) * int(cart[str(bijuterie.id)]))
        }
        for bijuterie in bijuterii
    ]

    return render(request, 'bijuterii/checkout.html', {
        'cart_items': cart_items,
        'cart': cart,
    })


def remove_bijuterie_from_cart(request, bijuterie_id):
    get_object_or_404(Bijuterie, pk=bijuterie_id)

    cart = Cart(request)
    cart.remove(bijuterie_id)

    return redirect(reverse('bijuterii:checkout'))
