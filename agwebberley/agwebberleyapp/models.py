from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime, date

class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	post_date = models.DateField()
	post_update_date = models.DateField()
	body = models.TextField()
	download1n = models.CharField(max_length=255, blank=True)
	download1 = models.CharField(max_length=255, blank=True)
	download2n = models.CharField(max_length=255, blank=True)
	download2 = models.CharField(max_length=255, blank=True)

	def __str__(self):
		return self.title + ' | ' + str(self.author)

	def get_absolute_url(self):
		return reverse('article-detail', args=(str(self.id)))

