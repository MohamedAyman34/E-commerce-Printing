from django.contrib import admin
from .models import Order ,Order_Detail ,OrderType,Ordersize
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.


class OrderTypeInline(admin.TabularInline):
    model = OrderType
class OrderSizeInline(admin.TabularInline):
    model = Ordersize

class OrderAdmin(SummernoteModelAdmin):
    inlines = [OrderTypeInline,OrderSizeInline]
    summernote_fields = '__all__'



admin.site.register(Order)
admin.site.register(Order_Detail,OrderAdmin)
