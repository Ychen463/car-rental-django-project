from django.contrib import admin

# Register your models here.
from .models import Account


class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'user_id', 'user_type',
                    'city', 'create_date')
    list_display_links = ('user_id', 'first_name', 'last_name')
    search_fields = ('first_name', 'last_name', 'email')
    list_per_page = 25


admin.site.register(Account, AccountAdmin)
