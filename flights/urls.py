# posts/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.FlightList.as_view()),
    path('<int:pk>/', views.FlightDetail.as_view()),
    path('', views.PlayerList.as_view()),
    path('<int:pk>/', views.PlayerDetail.as_view()),
    path('', views.CellList.as_view()),
    path('<int:pk>/', views.CellDetail.as_view()),

]