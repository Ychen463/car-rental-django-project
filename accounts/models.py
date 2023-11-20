from django.db import models
from datetime import datetime

# Create your models here.

INDIVIDUAL = 'Individual'
ENTERPRISE = 'Enterprise'
USER_TYPE_CHOICES = [
    (INDIVIDUAL, 'Individual'),
    (ENTERPRISE, 'Enterprise'),
]


class Account(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    message = models.TextField(blank=True)
    user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=INDIVIDUAL,
    )

    def __str__(self):
        return self.email
