from django.urls import path
from django.core.paginator import  Paginator
from verighete.views import show_all_verighete, show_modelverighete_details, add_modelverighete_to_cart

app_name='verighete'

urlpatterns = [
    path('', show_all_verighete, name='all'),
    path ( '<int:modelverighete_id>/' , show_modelverighete_details , name='details' ) ,
    path ( '<int:modelverighete_id>/add_to_cart' , add_modelverighete_to_cart , name='add_to_cart' ) ,
]