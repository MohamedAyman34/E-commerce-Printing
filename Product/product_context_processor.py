from .models import Product , Category
from django.db.models import F , Q

def get_product(request):
    queryset1 = Product.objects.filter(category__name="DOCUMENT PRINTING")
    queryset2 = Product.objects.filter(category__name="BUSINESS ESSENTIALS")
    queryset3 = Product.objects.filter(category__name="SPECIALTY PRINTS & SERVICES")
    queryset4 = Product.objects.filter(category__name="MARKETING MATERIALS")
    queryset5 = Product.objects.filter(category__name="PROMOTIONAL PRODUCTS")
    queryset6 = Product.objects.filter(category__name="BANNERS")
    queryset7 = Product.objects.filter(category__name="SIGNS")
    queryset8 = Product.objects.filter(category__name="POSTERS")
    queryset9 = Product.objects.filter(category__name="PHOTOS")
    queryset10 = Product.objects.filter(category__name="WALL ART & FRAMES")
    queryset11 = Product.objects.filter(category__name="Cards & Invitations")


    return {'c_product1':queryset1,'c_product2':queryset2,'c_product3':queryset3
            ,'c_product4':queryset4,'c_product5':queryset5,'c_product6':queryset6
            ,'c_product7':queryset7,'c_product8':queryset8,'c_product9':queryset9
            ,'c_product10':queryset10,'c_product11':queryset11}
   