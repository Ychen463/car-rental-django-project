from django.contrib import admin
from .models import Order

# Register your models here.


class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_title', 'first_name', 'last_name', 'email',
                    'pickup_date', 'dropoff_date', 'pickup_location', 'dropoff_location', 'create_date')
    list_display_links = ('id', 'first_name', 'last_name',
                          'pickup_date', 'pickup_location', 'create_date')
    search_fields = ('first_name', 'last_name', 'car_id', 'pickup_date')
    list_per_page = 25


admin.site.register(Order, OrderAdmin)
