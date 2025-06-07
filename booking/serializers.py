from rest_framework import serializers
from .models import Fitness, Booking


class FitnessClassSerializers(serializers.ModelSerializer):
    class Meta:
        model = Fitness
        fields = ['id', 'name', 'start_time', 'instructor', 'available_slots']

class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = ['id', 'fitness_class', 'client_name', 'client_email', 'booked_at']