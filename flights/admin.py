from django.contrib import admin
from .models import Seat, Passenger, Flight
# Register your models here.
admin.site.register(Seat)
admin.site.register(Passenger)
admin.site.register(Flight)