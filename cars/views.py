from django.shortcuts import render, get_object_or_404
# from .models import Car
# from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
# Create your views here.


def cars(request):
    # cars = Car.objects.order_by('-created_date')
    # paginator = Paginator(cars, 4)
    # page = request.GET.get('page')
    # paged_cars = paginator.get_page(page)
    # model_search = Car.objects.values_list('model', flat=True).distinct()
    # city_search = Car.objects.values_list('city', flat=True).distinct()
    # year_search = Car.objects.values_list('year', flat=True).distinct()
    # body_style_search = Car.objects.values_list(
    #     'body_style', flat=True).distinct()
    # transmission_search = Car.objects.values_list(
    #     'transmission', flat=True).distinct()
    # data = {
    #     'cars': paged_cars,
    #     'model_search': model_search,
    #     'city_search': city_search,
    #     'year_search': year_search,
    #     'body_style_search': body_style_search,
    # }
    # return render(request, 'cars/cars.html', data)
    return render(request, 'cars/cars.html')
