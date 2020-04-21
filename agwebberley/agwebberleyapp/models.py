from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
	title = models.CharField(max_length=255)
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	body = models.TextField()
	download1n = models.TextField(default="Download1 Name}")
	download1 = models.TextField(default="Download1 Link")
	download2n = models.TextField(default="Download2 Name")
	download2 = models.TextField(default="Download2 Link")

	def __str__(self):
		return self.title + ' | ' + str(self.author)