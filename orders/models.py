from django.db import models
from datetime import datetime

from contacts.models import Contact
from cars.models import Car

# Create your models here.


class Order(models.Model):

    # user = models.ForeignKey(Contact, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    user_id = models.IntegerField(blank=True, null=True)

    car_id = models.IntegerField(default=1)
    car_title = models.CharField(max_length=100, null=True, blank=True)
    pickup_date = models.DateField(blank=True, default=datetime.now)
    dropoff_date = models.DateField(blank=True, default=datetime.now)
    pickup_location = models.CharField(max_length=100, null=True, blank=True)
    dropoff_location = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)

    state = models.CharField(max_length=100, null=True, blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    phone = models.CharField(max_length=100, null=True, blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)

    def __str__(self):
        return f"Order {self.id} by {self.first_name}"
