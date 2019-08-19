from django.db import models

# Create your models here.

class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Passenger(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Seat(models.Model):
    seatnumber = models.CharField(max_length=3)
    flight = models.ForeignKey('Flight', default=1, on_delete=models.CASCADE)
    passenger = models.OneToOneField('Passenger', default=1, on_delete=models.CASCADE)
    

    def __str__(self):
        return self.seatnumber
