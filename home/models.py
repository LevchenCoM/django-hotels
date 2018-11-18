from django.db import models
from django.core.validators import URLValidator

# Create your models here.
class NavigationMenuLinks(models.Model):
    order_num  = models.IntegerField(default=0)
    label = models.CharField(max_length=64, blank=False)
    url   = models.TextField(max_length=128)

    def __str__(self):
        return "{} : {}".format(self.label, self.url)

    class Meta:
        verbose_name = "Navigation menu link"
        verbose_name_plural = "Navigation menu links"
