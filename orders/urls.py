from django.urls import path
from .views import add_to_cart 


app_name = "Order"

urlpatterns = [
    path('cart/add',add_to_cart,name='add_to_cart'), 
    # path('cart/delete',item_delete,name='item_delete'), 
]
