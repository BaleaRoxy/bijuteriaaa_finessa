from django.urls import path
from django.core.paginator import  Paginator
from lingouri.views import show_all_lingouri, show_lingou_details, add_lingou_to_cart

app_name='lingouri'

urlpatterns = [
    path('', show_all_lingouri, name = 'all'),
    path ( '<int:lingou_id>/' , show_lingou_details , name='details' ) ,
    path ( '<int:lingou_id>/add_to_cart' , add_lingou_to_cart , name='add_to_cart' ) ,
]