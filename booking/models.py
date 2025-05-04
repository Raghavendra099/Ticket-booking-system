from django.db import models
from django.utils import timezone  # Import the timezone module

# Define the transport type choices as constants
TRANSPORT_CHOICES = [
    ('flight', 'Flight'),
    ('train', 'Train'),
    ('bus', 'Bus'),
]

class Ticket(models.Model):
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    passenger_name = models.CharField(max_length=100)
    journey_date = models.DateField(default=timezone.now)  # Uses timezone.now
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10, default="UNASSIGNED")
    booking_date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.passenger_name} - {self.source} to {self.destination}"

# Flight Model (with airline_name)
class Flight(models.Model):
    airline_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.DateTimeField()
    arrival_time = models.DateTimeField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Flight from {self.source} to {self.destination} on {self.departure_time}"

class Train(models.Model):
    train_name = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return self.train_name
# Bus Model
# booking/models.py

class Bus(models.Model):
    bus_operator = models.CharField(max_length=100)
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    departure_time = models.CharField(max_length=100)
    arrival_time = models.CharField(max_length=100)
    price = models.IntegerField()

    def __str__(self):
        return f"{self.bus_operator} - {self.source} to {self.destination}"


# Ticket Model (reference to Flight, Train, or Bus)
class Ticket(models.Model):
    transport_type = models.CharField(max_length=10, choices=TRANSPORT_CHOICES)
    passenger_name = models.CharField(max_length=100)
    journey_date = models.DateField()
    source = models.CharField(max_length=100)
    destination = models.CharField(max_length=100)
    seat_number = models.CharField(max_length=10)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    is_confirmed = models.BooleanField(default=False)
    transport = models.ForeignKey('Flight', on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return f"Ticket for {self.passenger_name} from {self.source} to {self.destination}"
