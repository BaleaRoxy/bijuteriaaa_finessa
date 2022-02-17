from django.urls import path
from django.core.paginator import  Paginator
from lanturi.views import show_all_lanturi, show_lant_details, add_lant_to_cart

app_name='lanturi'

urlpatterns = [
    path('', show_all_lanturi, name = 'all'),
    path ( '<int:lant_id>/' , show_lant_details , name='details' ) ,
    path ( '<int:lant_id>/add_to_cart' , add_lant_to_cart , name='add_to_cart' ) ,
]