from django.shortcuts import render
from .models import Field, Booking

def field_list(request):
    fields = Field.objects.all()
    bookings = Booking.objects.all()
    booked_dates = [booking for booking in bookings]
    available_fields = [field for field in fields if field not in booked_dates]
    return render(request, 'fut_pole/field_list.html', {'available_fields': available_fields})
