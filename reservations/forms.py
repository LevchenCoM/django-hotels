from django import forms

from .models import Reservation, ApartmentInReservation

class PreReservationForm(forms.ModelForm):

    class Meta:
        model = Reservation
        localized_fields = ('customer_name', 'customer_phone','customer_email', 'comments')
