from django.urls import path
from django.core.paginator import  Paginator
from bijuterii.views import show_all_bijuterii, show_bijuterie_details, add_bijuterie_to_cart, show_checkout, remove_bijuterie_from_cart


app_name='bijuterii'

urlpatterns = [
    path ('', show_all_bijuterii, name='all' ) ,
    path ('<int:bijuterie_id>/' , show_bijuterie_details , name='details'),
    path('<int:bijuterie_id>/add_to_cart', add_bijuterie_to_cart, name='add_to_cart'),
    path('checkout/', show_checkout, name='checkout'),
    path('<int:bijuterie_id>/remove_from_cart/', remove_bijuterie_from_cart, name='remove_from_cart'),
]

