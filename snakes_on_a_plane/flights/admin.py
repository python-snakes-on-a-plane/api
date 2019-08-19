from django.contrib import admin
from .models import Seats, Passenger, Flight
# Register your models here.
admin.site.register(Seats)
admin.site.register(Passenger)
admin.site.register(Flight)