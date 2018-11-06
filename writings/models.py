from django.db import models
from django.core.urlresolvers import reverse
from accounts.models import User


class Writing(models.Model):
	owner = models.ForeignKey(User, on_delete=models.CASCADE)
	title = models.CharField(max_length=150)
	body = models.TextField()
	category = models.CharField(max_length=100)
	timestamp = models.DateTimeField(auto_now= True)




	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return "/writings/%i" %self.id
