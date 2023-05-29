from django.contrib import admin
from .models import Profile , UserPhoneNumbers , UserAddress
# Register your models here.


admin.site.register(Profile)
admin.site.register(UserPhoneNumbers)
admin.site.register(UserAddress)
