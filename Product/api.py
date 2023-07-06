#view
from .serializers import ProductSerializer
from .models import Product
from rest_framework import generics



class ProductList_api(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()


class ProductDetail_api(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = ProductSerializer
    queryset = Product.objects.all()