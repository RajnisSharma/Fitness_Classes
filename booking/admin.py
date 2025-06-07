from django.contrib import admin
from .models import Fitness, Booking

# Register your models here.
@admin.register(Fitness)
class FitnessClassAdmin(admin.ModelAdmin):
    list_display = ('name', 'start_time', 'instructor', 'available_slots')

@admin.register(Booking)
class BookingClassAdmin(admin.ModelAdmin):
    list_display = ('fitness_class', 'client_name', 'client_email', 'booked_at')