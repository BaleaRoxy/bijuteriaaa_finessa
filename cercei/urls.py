from django.urls import path
from django.core.paginator import  Paginator
from cercei.views import show_all_cercei, show_modelcercei_details, add_modelcercei_to_cart

app_name='cercei'


urlpatterns = [
    path('', show_all_cercei, name = 'all'),
    path ( '<int:modelcercei_id>/' , show_modelcercei_details , name='details' ) ,
    path ( '<int:modelcercei_id>/add_to_cart' , add_modelcercei_to_cart , name='add_to_cart' ) ,
]