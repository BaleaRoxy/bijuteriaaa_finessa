from django.urls import path
from django.core.paginator import  Paginator
from bratari.views import show_all_bratari, show_bratara_details, add_bratara_to_cart

app_name='bratari'

urlpatterns = [
    path ('', show_all_bratari, name='all' ) ,
    path ('<int:bratara_id>/' , show_bratara_details , name='details'),
    path('<int:bratara_id>/add_to_cart', add_bratara_to_cart, name='add_to_cart'),
]

