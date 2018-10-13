from django.db import models
from django.contrib.auth.models import User

from django.conf import settings


class Message(models.Model):
	author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='messages')
	text = models.TextField(max_length=300)
	pub_date = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return ' - '.join([self.author.username, self.text])

	class Meta:
		ordering = ('-pub_date',)


class Follow(models.Model):
	who = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='whos_tweets')
	whom = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

	def __str__(self):
		return self.who.username + ' -> ' + self.whom.username

	class Meta:
		unique_together = ("who", "whom",)
