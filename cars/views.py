from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def cars(request):
    cars = Car.objects.order_by('-created_date')
    paginator = Paginator(cars, 4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    pickup_location_serach = Car.objects.values_list(
        'pickup_location', flat=True).distinct()
    dropoff_location_serach = Car.objects.values_list(
        'dropoff_location', flat=True).distinct()
    pickup_avail_locations = Car.objects.values_list(
        'pickup_location', flat=True).all()  # Replace with your actual model and query

    pickup_date_search = Car.objects.values_list(
        'pickup_date', flat=True).distinct()
    pickup_avail_dates = Car.objects.values_list(
        'pickup_date', flat=True).all()
    dropoff_date_search = Car.objects.values_list(
        'dropoff_date', flat=True).distinct()

    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list(
        'transmission', flat=True).distinct()
    data = {
        'cars': paged_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'pickup_location_serach': pickup_location_serach,
        'dropoff_location_serach': dropoff_location_serach,
        'pickup_date_serach': pickup_date_search,
        'dropoff_date_serach': dropoff_date_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/cars.html', data)


def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)
    pickup_location_serach = Car.objects.values_list(
        'pickup_location', flat=True).distinct()
    dropoff_location_serach = Car.objects.values_list(
        'dropoff_location', flat=True).distinct()
    data = {
        'single_car': single_car,
        'pickup_location_serach': pickup_location_serach,
        'dropoff_location_serach': dropoff_location_serach,
    }

    return render(request, 'cars/car_detail.html', data)


def search(request):
    cars = Car.objects.order_by('-created_date')
    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    pickup_location_serach = Car.objects.values_list(
        'pickup_location', flat=True).distinct()
    dropoff_location_search = Car.objects.values_list(
        'dropoff_location', flat=True).distinct()
    pickup_date_search = Car.objects.values_list(
        'pickup_date', flat=True).distinct()
    dropoff_date_search = Car.objects.values_list(
        'dropoff_date', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list(
        'body_style', flat=True).distinct()
    transmission_search = Car.objects.values_list(
        'transmission', flat=True).distinct()

    if 'keyword' in request.GET:
        keyword = request.GET['keyword']
        if keyword:
            cars = cars.filter(description__icontains=keyword)

    if 'model' in request.GET:
        model = request.GET['model']
        if model:
            cars = cars.filter(model__icontains=model)

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            cars = cars.filter(city__iexact=city)
    if 'pickup_loacation' in request.GET:
        pickup_loacation = request.GET['pickup_location']
        if pickup_loacation:
            cars = cars.filter(pickup_loacation__iexact=pickup_loacation)
    if 'dropoff_loacation' in request.GET:
        dropoff_location = request.GET['dropoff_location']
        if dropoff_location:
            cars = cars.filter(dropoff_locationn__iexact=dropoff_location)
    if 'pickup_date' in request.GET:
        pickup_date = request.GET['pickup_date']
        if pickup_date:
            cars = cars.filter(pickup_date__lte=pickup_date)
    if 'dropoff_date' in request.GET:
        dropoff_date = request.GET['dropoff_date']
        if dropoff_date:
            cars = cars.filter(pickup_date__gte=dropoff_date)
    if 'year' in request.GET:
        year = request.GET['year']
        if year:
            cars = cars.filter(year__iexact=year)

    if 'body_style' in request.GET:
        body_style = request.GET['body_style']
        if body_style:
            cars = cars.filter(body_style__iexact=body_style)

    if 'min_price' in request.GET:
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']
        if max_price:
            cars = cars.filter(price__gte=min_price, price__lte=max_price)

    data = {
        'cars': cars,
        'model_search': model_search,
        'city_search': city_search,
        'pickup_location_search': pickup_location_serach,
        'dropoff_location_search': dropoff_location_search,
        'pickup_date_search': pickup_date_search,
        'dropoff_date_search': dropoff_date_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }
    return render(request, 'cars/search.html', data)
