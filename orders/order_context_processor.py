from .models import Order , Order_Detail
from django.shortcuts import render , redirect
from django.views.generic import DeleteView
from django.core.mail import send_mail



def get_or_create_order(request):
    
    if request.user.is_authenticated: 
        cart , create = Order.objects.get_or_create(user=request.user)
        crt_detail = Order_Detail.objects.filter(order=cart.id)
        return {'cart':cart , 'crt_detail':crt_detail}


def delete_item(request):
    if request.method == "POST":
        item_id = request.POST['itemid']
        cart_detail = Order_Detail.objects.get(id=item_id)
        Order_Detail.delete(cart_detail)
        
        