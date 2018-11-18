from django.contrib import admin
from .models import *
# Register your models here.

class ApartmentInReservationInline(admin.TabularInline):
    model = ApartmentInReservation
    extra = 0

class StatusAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Status._meta.fields]

    class Meta:
        model = Status


admin.site.register(Status,StatusAdmin)

class ReservationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Reservation._meta.fields]
    inlines = [ApartmentInReservationInline]
    class Meta:
        model = Reservation


admin.site.register(Reservation,ReservationAdmin)

class ApartmentInReservationAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ApartmentInReservation._meta.fields]

    class Meta:
        model = ApartmentInReservation


admin.site.register(ApartmentInReservation,ApartmentInReservationAdmin)

@admin.register(ReservedDates)
class ReservedDatesAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ReservedDates._meta.fields]

    class Meta:
        model = ReservedDates
