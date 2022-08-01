from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(default=0)
	address = models.CharField(max_length=255, default='ssd')
	mobile_number = models.CharField(max_length=12, default=0)
	pincode = models.PositiveIntegerField(default=0)
