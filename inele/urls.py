from django.urls import path
from django.core.paginator import  Paginator
from inele.views import show_all_inele, show_inel_details, add_inel_to_cart

app_name='inele'

urlpatterns = [
    path('', show_all_inele, name = 'all'),
    path ( '<int:inel_id>/' , show_inel_details , name='details' ) ,
    path ( '<int:inel_id>/add_to_cart' , add_inel_to_cart , name='add_to_cart' ) ,
]