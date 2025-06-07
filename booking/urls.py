from django.urls import path
from . import views

urlpatterns = [
    path('classes/', views.List_Classes, name='classes'),
    path('book/', views.List_Booking, name='list_booking'),
    path('booking/', views.Create_booking, name='create_booking')
]
