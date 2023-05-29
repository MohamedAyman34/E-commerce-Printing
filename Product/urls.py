from django.urls import path
from .views import Product_detail 

app_name = "Product"

urlpatterns = [
    path('<slug:slug>/' , Product_detail.as_view(), name='product_detail'),
    
]
