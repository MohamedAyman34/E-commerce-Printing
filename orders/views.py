from django.shortcuts import render , redirect
from .models import Order ,Order_Detail,OrderType,Ordersize
from Product.models import Product
# Create your views here.


def add_to_cart(request):
    if request.method == 'POST':
        product_id = request.POST['productid']
        quantity = request.POST['quantity']
        photo =  request.FILES.get('photo',False)
        orientation = request.POST['orientation']
        print_color = request.POST['print_color']
        side = request.POST['side']
        Type = request.POST['Type']
        size = request.POST['size']
    
        product = Product.objects.get(id=product_id)
        cart = Order.objects.get(user=request.user)
        Order_Detail.objects.create(
            order = cart,
            product = product,
            orientation = orientation,
            print_color = print_color,
            side = side,
            quantity = int(quantity),
            price = product.price,
            photo = photo,
            total = int(quantity) * round(product.price,2)
        )
       
        order_detail = Order_Detail.objects.last()
        
        OrderType.objects.create(
            order_detail= order_detail,
            Type = Type,
        )
        Ordersize.objects.create(
            order_detail= order_detail,
            size = size,
        )
        return redirect(f'/products/{product.slug}')

# def item_delete(request,id):
#     if request.method == "POST":
#         print("Good Job")