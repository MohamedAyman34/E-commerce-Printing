from django.shortcuts import render
from Product.models import Category
from django.db.models import Count
# from Product.models import Category

# Create your views here.

def home(request):
    categories = Category.objects.all().annotate(product_count = Count('product_category'))
    return render(request,'Home/home.html',{"categories":categories})

