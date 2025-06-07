from django.shortcuts import render, get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.utils import timezone
from rest_framework import status
from .models import Fitness, Booking
from .serializers import FitnessClassSerializers, BookingSerializer

# Create your views here.
@api_view(['GET'])
def List_Classes(request):
    now = timezone.now()
    upcoming = Fitness.objects.filter(start_time__gt=now)
    serializer = FitnessClassSerializers(upcoming, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def Create_booking(request):
    data = request.data
    class_id = data.get('class_id')
    name = data.get('client_name')
    email = data.get('client_email')

    if class_id is None or name is None or email is None:
        return Response({'error':'class_id, client_name, client_email is required'},
                        status=status.HTTP_400_BAD_REQUEST)
    fitness_class = get_object_or_404(Fitness, id=class_id)
    
    if fitness_class.available_slots <= 0:
        return Response({'error':'No slots availabe in this class'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    already = Booking.objects.filter(
        client_email=email,
        fitness_class__start_time=fitness_class.start_time
    ).exists()
    if already:
        return Response({'error':'You have already booked a class at this time'},
                        status=status.HTTP_400_BAD_REQUEST)
    
    fitness_class.available_slots -= 1
    fitness_class.save()

    booking = Booking.objects.create(
        fitness_class=fitness_class,
        client_name = name,
        client_email = email
    )
    return Response({'status':"booked","booking_id":booking.id},
                    status=status.HTTP_201_CREATED)
@api_view(['GET'])
def List_Booking(request):
    email = request.query_params.get('email')
    if not email:
        return Response({'error':'Email query parameter is required'},
                        status=status.HTTP_400_BAD_REQUEST)
    bookings = Booking.objects.filter(client_email=email).order_by("booked_at")
    serializer = BookingSerializer(bookings, many=True)
    return Response(serializer.data)