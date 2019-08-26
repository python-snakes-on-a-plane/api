from django.db import models

# Create your models here.

class Flight(models.Model):
    name = models.CharField(max_length=256)
    airborne = models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Seat(models.Model):
    seatnumber = models.CharField(max_length=3)
    flight = models.ForeignKey('Flight', default=1, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.seatnumber

class Passenger(models.Model):
    name = models.CharField(max_length=256)
    seat = models.OneToOneField('Seat', default=1, on_delete=models.CASCADE, related_name='passenger')
    flight = models.ForeignKey('Flight', default=1, on_delete=models.CASCADE, related_name='flight')


    def __str__(self):
        return self.name, self.seat, self.flight

class Player(Passenger):
    user_name = models.Charfield(max_length=256)

    def __str__(self):
        return self.user_name

class Cell(models.Model):
    cell_type = models.Charfield(max_length=256)
    x_pos = models.Charfield(max_length=10)
    y_pos = models.Charfield(max_length=10)

    def __str__(self):
        return self.cell_type, self.x_pos, self.y_pos


