from django.db import models

# Create your models here.

class Flight(models.Model):
    name = models.CharField(max_length=256)



class Passenger(models.Model):
    name = models.CharField(max_length=256)
    
    def __str__(self):
        return self.name

class Seats(models.Model):
    seatnumber = models.CharField(max_length=3)
    passenger = models.ForeignKey('Passenger', default=1, on_delete=models.CASCADE)

    def __str__(self):
        return self.seatnumber
