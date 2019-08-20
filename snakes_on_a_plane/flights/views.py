from django.shortcuts import render

# Create your views here.
# posts/views.py
from rest_framework import generics

from .models import Flight
from .serializers import FlightSerializer


class FlightList(generics.ListCreateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class FlightDetail(generics.RetrieveUpdateAPIView):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer

# Create your views here.
