from rest_framework import serializers
from . import models


class FlightSerializer(serializers.ModelSerializer):

    class Meta:
        fields = ('id', 'name',)
        model = models.Flight