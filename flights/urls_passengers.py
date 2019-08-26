from django.urls import path
from . import views

urlpatterns = [
    
    path('', views.PassengerList.as_view()),
    path('<int:pk>/', views.PassengerDetail.as_view()),

]