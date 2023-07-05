from django.urls import path
from .views import Product_detail 
from .api import ProductList_api , ProductDetail_api

app_name = "Product"

urlpatterns = [
    path('<slug:slug>/' , Product_detail.as_view(), name='product_detail'),
    

    #api
    path('api' , ProductList_api.as_view()),
    path('api/<int:pk>' , ProductDetail_api.as_view()),




]
