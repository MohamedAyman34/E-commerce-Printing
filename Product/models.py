from django.db import models
from django.utils.translation import gettext as _
from django.utils.text import slugify


# Create your models here.

class Product(models.Model):
    name = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("image"), upload_to='Products/', height_field=None, width_field=None, max_length=None)
    description = models.TextField(_("Description") , max_length=10000)
    category = models.ForeignKey("Category", verbose_name=_("Category"),related_name='product_category', on_delete=models.SET_NULL ,null=True ,blank=True)
    price = models.FloatField(_("Price"))
    slug = models.SlugField(_("Slug"),null=True,blank=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super(Product,self).save( *args, **kwargs)

    def __str__(self) :
        return self.name

class Category(models.Model):
    name  = models.CharField(_("Name"), max_length=100)
    image = models.ImageField(_("Image"), upload_to='Category/')

    def __str__(self) :
        return self.name
