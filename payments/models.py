import datetime
from django.db import models
from orders.models import Order
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Payment(models.Model):
    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('Completed', 'Completed'),
        ('Failed', 'Failed'),
        # Add more statuses if needed
    ]
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, blank=True, null=True)
    amount = models.DecimalField(
        max_digits=10, decimal_places=2, blank=True, null=True)
    # e.g., 'Pending', 'Completed', 'Failed'
    status = models.CharField(
        max_length=100, choices=STATUS_CHOICES, blank=True, null=True)
    promo_code = models.CharField(max_length=100, blank=True, null=True)
    payment_token = models.CharField(max_length=100, blank=True, null=True)

    transaction_id = models.CharField(max_length=100, unique=True)
    create_date = models.DateTimeField(
        auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return f"Payment for Order {self.order.id}"


class PromoCode(models.Model):
    promo_code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.PositiveIntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(100)])
    valid_from = models.DateTimeField()
    valid_to = models.DateTimeField()
    max_uses = models.PositiveIntegerField(default=1)  # Added field
    used_times = models.PositiveIntegerField(default=0)  # Added field
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.promo_code

    def is_valid(self):
        # Logic to check if the promo code is valid (e.g., based on date and max uses)
        # ...
        return True  # Or False based on conditions


def is_valid(self):
    current_time = timezone.now()
    return (
        self.is_active and
        self.valid_from <= current_time <= self.valid_to and
        self.used_times < self.max_uses
    )
