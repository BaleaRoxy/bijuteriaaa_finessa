from django.urls import path
from django.core.paginator import  Paginator
from pandative.views import show_all_pandative, show_pandativ_details, add_pandativ_to_cart

app_name='pandative'

urlpatterns = [
    path('', show_all_pandative, name = 'all'),
    path ( '<int:pandativ_id>/' , show_pandativ_details , name='details' ) ,
    path ( '<int:pandativ_id>/add_to_cart' , add_pandativ_to_cart , name='add_to_cart' ) ,
]