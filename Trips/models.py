from django.db import models
from django.contrib.auth.models import User  
# Create your models here.

class OrganizerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    national_ID = models.CharField(max_length=50)
    bus_plate_number = models.CharField(max_length=30)
    organizer_company = models.CharField(max_length=450, null=True, blank=True)
    is_verified = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.user.username} - Organizer"


class TripInfo(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Approved', 'Approved'),
        ('Rejected', 'Rejected'),
    ]

    title = models.CharField(max_length=450)
    description = models.TextField()
    destination = models.CharField(max_length=700)
    departure_date = models.DateTimeField()
    return_date = models.DateTimeField()
    price = models.FloatField()
    created_by = models.ForeignKey(OrganizerProfile, on_delete=models.CASCADE)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return self.title


class Booking(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Delivered', 'Delivered'),
        ('Canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(TripInfo, on_delete=models.CASCADE)
    booking_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Pending')

    def __str__(self):
        return f"{self.user.username} - {self.trip.title}"


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    trip = models.ForeignKey(TripInfo, on_delete=models.CASCADE)
    comment = models.TextField()
    rating = models.PositiveSmallIntegerField(default=5) 
    def __str__(self):
        return f"{self.user.username} - {self.trip.title}"
    
