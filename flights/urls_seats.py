# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.SeatList.as_view()),
    path('<int:pk>/', views.SeatDetail.as_view()),

]