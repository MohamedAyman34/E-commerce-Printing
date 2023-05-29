from django.shortcuts import render
from .models import Product,Category
from django.db.models import F
from django.views.generic import ListView , DetailView
from orders.forms import OrderForm


# Create your views here.

class Product_detail(DetailView):
    model = Product


def new_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
    else:
        form = OrderForm()

    return render(request,'product/product_detail.html',{'form':form})
