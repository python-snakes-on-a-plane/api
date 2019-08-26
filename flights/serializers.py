from rest_framework import serializers
from . import models


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name',)
        model = models.Flight

class SeatSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'seatnumber',)
        model = models.Seat

class PassengerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('seat', 'name', 'flight')
        model = models.Passenger

class PlayerSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('username')
        model = models.Player

class CellSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('cell_type')
        model = models.Cell