from django.contrib import admin
# from django_summernote.admin import SummernoteModelAdmin
from .models import Product,Category

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)