from django.db import models
from datetime import datetime
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User
from django.db import models

# Create your models here.

INDIVIDUAL = 'Individual'
ENTERPRISE = 'Enterprise'
USER_TYPE_CHOICES = [
    (INDIVIDUAL, 'Individual'),
    (ENTERPRISE, 'Enterprise'),
]


class Account(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, blank=True, default=1)

    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    phone = models.CharField(max_length=100)
    # user_id = models.IntegerField(blank=True)
    create_date = models.DateTimeField(blank=True, default=datetime.now)
    user_type = models.CharField(
        max_length=10,
        choices=USER_TYPE_CHOICES,
        default=INDIVIDUAL,
    )

    def __str__(self):
        return self.email
