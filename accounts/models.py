from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse_lazy

class CustomUser(AbstractUser):
	age = models.PositiveIntegerField(null=True, blank=True)
	bio = models.CharField(max_length=200, null=True, blank=True)

	def get_absolute_url(self):
		return reverse_lazy('profile', args=(self.pk,))
