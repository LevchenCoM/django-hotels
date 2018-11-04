from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound
from apartments.models import Apartment, ApartmentImage, ApartmentDates
from reservations.models import Reservation, Status, ApartmentInReservation
from datetime import datetime, date
from django.core.mail import send_mail
# Create your views here.
def apartment(request, apartment_id):
    try:
        apartment = Apartment.objects.get(id=apartment_id)
    except:
        return HttpResponseNotFound()
    apartment_images = ApartmentImage.objects.filter(apartment_id=apartment_id).order_by("number_of_image")
    disableDatesSet = ApartmentDates.objects.filter(date__gte=datetime.today(), is_active=True)
    disableDates = []
    for d_date in disableDatesSet:
        disableDates.append('{}/{}/{}'.format(d_date.date.day, d_date.date.month, d_date.date.year))
    # test_date = "{}/{}/{}".format(test_date.day, test_date.month, test_date.year)
    # print(test_date)
    context = {'apartment':apartment,'apartment_images': apartment_images, 'disableDates':disableDates}
    if request.method == "POST":
        check_in = datetime.strptime(request.POST['check_in'],'%d/%m/%y')
        check_out = datetime.strptime(request.POST['check_out'],'%d/%m/%y')
        delta = check_out - check_in
        total_price = apartment.price*delta.days
        reservation = Reservation(customer_name=request.POST['name'],
                                  customer_email=request.POST['email'],
                                  customer_phone=request.POST['tel_full'],
                                  status=Status.objects.get(name='Pre-reservation'),
                                  check_in_date=check_in,
                                  check_out_date=check_out,
                                  total_price=total_price,
                                  comments = request.POST['comments'])
        reservation.save()
        apartment_in_reservation = ApartmentInReservation(reservation=reservation,
                                                         apartment=apartment, num=delta.days,
                                                         price_per_item=apartment.price,
                                                         total_price=total_price)
        apartment_in_reservation.save()
        send_mail(
            'Subject here',
            'Here is the message.',
            'sender@gmail.com',
            ['1@gmail.com'],
            fail_silently=False,)
    return render(request,'apartment.html',context)
