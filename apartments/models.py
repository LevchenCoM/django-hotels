from django.db import models
from tinymce import models as tinymce_models

class Apartment(models.Model):
    is_active  = models.BooleanField(default=True)
    name = models.CharField(max_length=64, blank=True, null=True)
    short_description = models.TextField(max_length=200, blank=True, null=True)
    # description = models.TextField(blank=True, null=True)
    description = tinymce_models.HTMLField()
    price = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    special_offer = models.BooleanField(default=False)
    special_price = models.DecimalField(max_digits=10,decimal_places=2, default=0)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return " {}".format(self.name)

    class Meta:
        verbose_name = "apartment"
        verbose_name_plural = "apartments"

class ApartmentImage(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete= models.CASCADE,blank=True, null=True, default=None)
    image = models.ImageField(upload_to='product_images/')
    number_of_image = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Image"
        verbose_name_plural = "Images"
        ordering = ['number_of_image']

# class ApartmentDates(models.Model):
#     DISABLE = '0'
#     BOOKED = '1'
#     STATUS_CHOICES = (
#         (DISABLE, 'Disable'),
#         (BOOKED, 'Booked'),
#     )
#     status = models.CharField(max_length=1,
#                                       choices=STATUS_CHOICES,
#                                       default=DISABLE)
#     apartment   = models.ForeignKey(Apartment, on_delete= models.CASCADE, blank=True, null=True, default=None)
#     date = models.DateField(null=True)
#     is_active = models.BooleanField(default=True)
#     # reservation  = models.ForeignKey(Reservation, on_delete= models.SET_NULL, blank=True, null=True, default=None)
#     created = models.DateTimeField(auto_now_add=True, auto_now=False)
#     updated = models.DateTimeField(auto_now_add=False, auto_now=True)
#
#     class Meta:
#         verbose_name = "Date statuses"
#         verbose_name_plural = "Dates statuses"
#         unique_together = ("date", "apartment")

class Property(models.Model):
    name = models.CharField(max_length=32, blank=False, null=False, default=None)

    def __str__(self):
        return " {}".format(self.name)

    class Meta:
        verbose_name = "Property"
        verbose_name_plural = "Properties"

class ApartmentProperty(models.Model):
    apartment = models.ForeignKey(Apartment, on_delete= models.CASCADE,blank=False, null=True, default=None)
    property = models.ForeignKey(Property, on_delete= models.CASCADE,blank=False, null=True, default=None)
    value = models.CharField(max_length=48, blank=True, null=False, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Apartment property"
        verbose_name_plural = "Apartments properties"
