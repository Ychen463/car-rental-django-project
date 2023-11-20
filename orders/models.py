from django.db import models
from datetime import datetime

from django.shortcuts import redirect, render

from django.contrib.auth.models import User
from cars.models import Car
from django.contrib import messages
# Create your models here.


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car = models.ForeignKey(
        Car, on_delete=models.CASCADE)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
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

    # price = models.DecimalField(
    #     max_digits=10, decimal_places=2, default=0.00)

    def total_days(self):
        if self.pickup_date and self.dropoff_date:
            return (self.dropoff_date - self.pickup_date).days
        return 0

    def total_amount(self):
        # Ensure you are accessing the unit_price from the Car model
        return self.total_days() * self.car.price

    def __str__(self):
        return f"Order {self.id} by {self.first_name}"

    def reserve(request):
        if request.method == 'POST':
            # Extract data from the form
            user_id = request.POST.get('user_id')
            car_id = request.POST.get('car_id')
            first_name = request.POST.get('first_name')
            last_name = request.POST.get('last_name')
            email = request.POST.get('email')
            phone = request.POST.get('phone')
            pickup_date = request.POST.get('pickup_date')
            dropoff_date = request.POST.get('dropoff_date')
            pickup_location = request.POST.get('pickup_location')
            dropoff_location = request.POST.get('dropoff_location')
            city = request.POST.get('city')
            state = request.POST.get('state')

            # Create or update the Order object
            created = Order.objects.update_or_create(
                user_id=user_id,
                car_id=car_id,
                defaults={
                    'first_name': first_name,
                    'last_name': last_name,
                    'email': email,
                    'phone': phone,
                    'pickup_date': pickup_date,
                    'dropoff_date': dropoff_date,
                    'pickup_location': pickup_location,
                    'dropoff_location': dropoff_location,
                    'city': city,
                    'state': state,
                }
            )
            created.save()
            if created:
                messages.success(request, 'Reservation created successfully.')
            else:
                messages.success(request, 'Reservation updated successfully.')

            return redirect('/cars/'+car_id)
        else:
            # Handle non-POST request here
            # return redirect('/cars/'+car_id)
            return render(request, 'cars/search.html', data)
