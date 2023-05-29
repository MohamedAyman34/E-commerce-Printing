from django.db import models
from utils.generator import generator
from django.contrib.auth.models import User
from django.utils import timezone
from django.utils.translation import gettext as _
from Product.models import Product
# Create your models here.
data_orientation = [
    ('Horizontal','Horizontal'),
        ('Vertical','Vertical')
]
data_side = [
    ('Single-Side','Single-Side'),
        ('Double-Side','Double-Side')
]
data_color = [
    ('Single-Side','Single-Side'),
        ('Double-Side','Double-Side')
]

class Order(models.Model):
    code = models.CharField(_("Code"), max_length=8 , default=generator)
    user = models.ForeignKey(User, verbose_name=_("User"),related_name='user_order', on_delete=models.CASCADE)
    order_time    = models.DateTimeField(_("Order Time"),default=timezone.now)

    def __str__(self):
        return f'order-{self.user}'

class Order_Detail(models.Model):
    order = models.ForeignKey(Order, verbose_name=_("Order"), related_name='order_orderDetail',on_delete=models.CASCADE)
    product = models.ForeignKey(Product, verbose_name="Product",related_name=_("OrderDetail_product"), on_delete=models.SET_NULL,null=True,blank=True)
    orientation = models.CharField(_("Orientation"), max_length=50,choices=data_orientation)
    print_color = models.CharField(_("Print Color"), max_length=50,choices=data_color)
    side = models.CharField(_("Side"), max_length=50,choices=data_side)
    quantity = models.FloatField(_("Quantity"))
    price = models.FloatField(_("Price"))
    photo = models.ImageField(_("Uploaded Photo"), upload_to='Uploaded Photo')

    def __str__(self):
        return f'order-{self.product}'
    

class OrderType(models.Model):
    order_detail = models.ForeignKey("Order_Detail", verbose_name=_("Order Detail Type"),related_name='order_type', on_delete=models.CASCADE)
    Type = models.CharField(_("Type"), max_length=50)

class Ordersize(models.Model):
    order_detail = models.ForeignKey("Order_Detail", verbose_name=_("Order Detail Size"),related_name='order_size', on_delete=models.CASCADE)
    size = models.CharField(_("Size"), max_length=50)