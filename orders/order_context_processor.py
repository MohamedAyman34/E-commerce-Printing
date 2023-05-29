from .models import Order , Order_Detail


def get_or_create_order(request):
    
    if request.user.is_authenticated:
        cart , create = Order.objects.get_or_create(user=request.user)
        crt_detail = Order_Detail.objects.filter(order=cart.id)
        return {'cart':cart , 'crt_detail':crt_detail}
