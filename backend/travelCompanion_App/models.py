from django.db import models
from django.contrib.auth.models import User

# Create your models here.

# Let us create model for collecting trip information of family members going for the trip with the user.

# Fields for capturing the details of family members (for example, spouse, children, others, trip purpose, departure date etc) are
# included 

class Trip(models.Model):
    spouse = models.CharField(max_length=100, null=True, blank=True)
    first_child = models.CharField(max_length=100, null=True, blank=True)
    second_child = models.CharField(max_length=100, null=True, blank=True)
    third_child = models.CharField(max_length=100, null=True, blank=True)
    others = models.CharField(max_length=100, null=True, blank=True)
    trip_purpose = models.TextField(max_length=500, null=True, blank=True)
    departure_date = models.DateField(blank=True, null=True)
    return_date = models.DateField(blank=True, null=True)
    departure_location = models.CharField(max_length=100, null=True, blank=True)
    destination_location = models.CharField(max_length=100, null=True, blank=True)
    
    
    # cost of trip
    trip_cost = models.CharField(max_length=100, null=True, blank=True)
    # set to current time
    created = models.DateTimeField(auto_now_add=True)
    # a field to mark whether a trip activity has ended or still active
    completed = models.BooleanField(default=False)
    
    #user who posted the trip details
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    
    
    def __str__(self):
        return self.trip_purpose
        

