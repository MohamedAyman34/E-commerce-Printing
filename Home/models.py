from django.db import models
from django.utils.translation import gettext as _

# Create your models here.

class Banner(models.Model):
    title = models.CharField(_("Banner Title"), max_length=100)
    image = models.ImageField(_("Baner Image"), upload_to='banner/', height_field=None, width_field=None, max_length=None)
    active = models.BooleanField(_("Active") , default=False)

    def __str__(self):
        return self.title

    
    