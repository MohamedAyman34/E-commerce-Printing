from django import forms
from .models import Order_Detail , OrderType,Ordersize


class OrderForm(forms.ModelForm):
    
    class Meta:
        model = Order_Detail
        fields = ("photo","orientation","print_color","side","quantity")

    class Meta:
        model = OrderType
        fields = ("Type",)

    class Meta:
        model = Ordersize
        fields = ("size",)

