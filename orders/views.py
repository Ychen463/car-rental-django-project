# Create your views here.
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact, Order
from django.contrib.auth.models import User

# Create your views here.


def inquiry(request):
    if request.method == 'POST':
        car_id = request.POST['car_id']
        car_title = request.POST['car_title']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        city = request.POST['city']
        state = request.POST['state']
        email = request.POST['email']
        phone = request.POST['phone']
        pickup_date = request.POST['pickup_date']
        dropoff_date = request.POST['dropoff_date']
        pickup_location = request.POST['pickup_location']
        dropoff_location = request.POST['dropoff_location']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(car_id=car_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, 'You have already made an inquiry about this car. Please wait until we get back to you.')
                return redirect('/cars/'+car_id)

        order = Order(car_id=car_id, car_title=car_title, user_id=user_id,
                      first_name=first_name, last_name=last_name,  city=city, state=state, email=email, phone=phone,
                      pickup_date=pickup_date, dropoff_date=dropoff_date, pickup_location=pickup_location, dropoff_location=dropoff_location)

        order.save()
        messages.success(
            request, 'Your request has been submitted, we will get back to you shortly.')
        return redirect('/cars/'+car_id)
