from django import forms
from bijuterii.models import Culoareaur, Bijuterie
# from payments.models import StripeCard

ORDER_BY_CHOICES = (('POPULARITY', 'Popularity'), ('PRICE_ASC', 'Price ascending'), ('PRICE_DESC', 'Price descending'))


def get_orderby_field(order_by):
    if order_by == 'PRICE_ASC':
        return 'price'

    if order_by == 'PRICE_DESC':
        return '-price'

    return 'id'


class FilterBijuterieForm(forms.Form):
    order_by = forms.ChoiceField(choices=ORDER_BY_CHOICES)
    culoriaur = forms.MultipleChoiceField(choices=(), widget=forms.CheckboxSelectMultiple, required=False)
    min_price = forms.DecimalField(max_digits=5, decimal_places=2, required=False)
    max_price = forms.DecimalField(max_digits=5, decimal_places=2, required=False)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        culoriaur = Culoareaur.objects.all()
        self.fields['culoriaur'].choices = tuple((culoareaur.id, culoareaur.name) for culoareaur in culoriaur)

    def clean_culoriaur(self):
        culoriaur = self.cleaned_data.get('culoriaur', [])
        return culoriaur

    def apply_filters(self):
        is_valid = self.is_valid()

        if is_valid:
            order_by = get_orderby_field(self.cleaned_data.get('order_by'))
            culoriaur = self.cleaned_data.get('culoriaur', [])
            min_price = self.cleaned_data.get('min_price')
            max_price = self.cleaned_data.get('max_price')
            #
            # print('culoriaur', culoriaur)
            # print('min_price', type(min_price))
            # print('max_price', type(max_price))

            bijuterii = Bijuterie.objects.order_by(order_by)

            if len(culoriaur) > 0:
                bijuterii = bijuterii.filter(culoriaur__id__in=culoriaur)

            if min_price:
                bijuterii = bijuterii.filter(price__gte=min_price)

            if max_price:
                bijuterii = bijuterii.filter(price__lte=max_price)

            return bijuterii

        return Bijuterie.objects.all()


class SelectCardForm(forms.Form):
    card = forms.ChoiceField(choices=(), widget=forms.RadioSelect)

    def __init__(self, user, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._user = user

        self.fields['card'].choices = tuple((card.id, card.number) for card in self._user.stripe_customer.cards.all())

    # def clean_card(self):
    #     card_id = self.cleaned_data['card']
    #
    #     try:
    #         card = StripeCard.objects.get(id=card_id)
    #     except StripeCard.DoesNotExist:
    #         card = None
    #
    #     if card is None:
    #         raise forms.ValidationError('Selected card is invalid.')
    #
    #     if card.stripe_customer.user.id != self._user.id:
    #         raise forms.ValidationError('Selected card is invalid.')
    #
    #     return card
    #
