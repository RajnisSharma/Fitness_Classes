from django.db import models

# Create your models here.
class Fitness(models.Model):
    name = models.CharField(max_length=100)
    start_time = models.DateTimeField()
    instructor = models.CharField(max_length=100)
    available_slots = models.PositiveIntegerField(default=11)

    def __str__(self):
        return f"{self.name} at {self.start_time} by {self.instructor}"
    
class Booking(models.Model):
    fitness_class = models.ForeignKey(Fitness, related_name='bookings', on_delete=models.CASCADE)
    client_name = models.CharField(max_length=100)
    client_email = models.EmailField()
    booked_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.client_name} booked {self.fitness_class.name}"