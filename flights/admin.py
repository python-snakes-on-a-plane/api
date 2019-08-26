from django.contrib import admin
from .models import Seat, Passenger, Flight, Player, Cell
# Register your models here.
admin.site.register(Seat)
admin.site.register(Passenger)
admin.site.register(Flight)
admin.site.register(Player)
admin.site.register(Cell)