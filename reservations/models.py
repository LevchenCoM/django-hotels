from django.db import models
from apartments.models import Apartment
from django.db.models.signals import post_save
from datetime import datetime, date, timedelta
# Create your models here.

class Status(models.Model):
    name = models.CharField(max_length=24, blank=True, null=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Status {}".format(self.name)

    class Meta:
        verbose_name = "Reservation status"
        verbose_name_plural = "Reservation statuses"

class Reservation(models.Model):
    customer_name = models.CharField(max_length=64, blank=True, null=True)
    customer_email = models.EmailField(blank=True, null=True)
    customer_phone = models.CharField(max_length=48, blank=True, null=True)
    comments = models.TextField(blank=True, null=True, default = None)
    status = models.ForeignKey(Status, on_delete= models.CASCADE)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0)  # Total amount of products in order
    check_in_date = models.DateField(null=True)
    check_out_date = models.DateField(null=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def set_booked_dates(self, apartment): #set 'BOOKED' status for selected days

        def book(date): #set 'BOOKED' status for param date for selected apartment
            new_book_date = ReservedDates(apartment=apartment, date=date, status='1', reservation=self) #status = booked
            try:
                new_book_date.save()
            except:
                print(("Can't book this date ({}) because it already booked").format(date))

        delta = (self.check_out_date - self.check_in_date).days
        current_date = self.check_in_date
        while current_date != self.check_out_date:
            book(current_date)
            current_date = current_date + timedelta(days=1)

    def __str__(self):
        return "Reservation {} {}".format(self.id, self.status)

    class Meta:
        verbose_name = "Reservation"
        verbose_name_plural = "Reservations"

class ApartmentInReservation(models.Model):
    reservation = models.ForeignKey(Reservation, on_delete= models.CASCADE, blank=True, null=True)
    apartment = models.ForeignKey(Apartment, on_delete= models.CASCADE, blank=True, null=True)
    num = models.IntegerField(default=0)
    price_per_item = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    total_price = models.DecimalField(max_digits=10, decimal_places=2,default=0) # num * price_per_item
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return "Apartment {}".format(self.apartment.name)

    class Meta:
        verbose_name = "Apartment in reservation"
        verbose_name_plural = "Apartments in reservation"

    # def save(self, *args, **kwargs):
    #     price_per_item = self.product.price
    #     self.price_per_item = price_per_item
    #     self.total_price = self.num * price_per_item
    #
    #     super(apartmentInReservation,self).save(*args, **kwargs)

class ReservedDates(models.Model):
    DISABLE = '0'
    BOOKED = '1'
    STATUS_CHOICES = (
        (DISABLE, 'Disable'),
        (BOOKED, 'Booked'),
    )
    status = models.CharField(max_length=1,
                                      choices=STATUS_CHOICES,
                                      default=DISABLE)
    apartment   = models.ForeignKey(Apartment, on_delete= models.CASCADE, blank=True, null=True, default=None)
    date = models.DateField(null=True)
    is_active = models.BooleanField(default=True)
    reservation  = models.ForeignKey(Reservation, on_delete= models.SET_NULL, blank=True, null=True, default=None)
    created = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    class Meta:
        verbose_name = "Reserved date"
        verbose_name_plural = "Reserved dates"
        unique_together = ("date", "apartment")

def apartment_in_reservation_postsave(sender, instance, created, **kwargs):
    pass
    # reservation = instance.reservation
    #
    # all_apartments_in_order = ApartmentInReservation.objects.filter(reservation=reservation, is_active = True)
    #
    # reservation_total_price = 0
    # for item in all_apartments_in_order:
    #     # print(item)
    #     reservation_total_price += item.total_price
    #
    # instance.apartment.total_price = reservation_total_price
    # instance.apartment.save(force_update=True)

post_save.connect(apartment_in_reservation_postsave, sender=ApartmentInReservation)
