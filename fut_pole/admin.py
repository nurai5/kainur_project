from django.contrib import admin
from .models import *

class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'owner', 'field', 'selected_date', 'selected_start_time', 'selected_end_time')


admin.site.register(Field)
admin.site.register(Owner)
admin.site.register(Booking, BookingAdmin)


