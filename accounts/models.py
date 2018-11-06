from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User


class User(AbstractUser):
	picture = models.ImageField(upload_to='images')
	gender = models.CharField(max_length=10)
	location = models.CharField(max_length=50)
	birth_date = models.DateField(null=True, blank=True)

	def __str__(self):
		return self.username



	def get_absolute_url(self):
		return "/accounts/profiles/%i" %self.id
