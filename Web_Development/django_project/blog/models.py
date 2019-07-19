from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from mdeditor.fields import MDTextField
from django.urls import reverse

# Create your models here.
class Category(models.Model):

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Tag(models.Model):

	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name


class Post(models.Model):

	title = models.CharField(max_length=100)
	posted_time = models.DateTimeField(default = timezone.now)
	author = models.ForeignKey(User, on_delete=models.CASCADE)

	content = MDTextField()

	category = models.ForeignKey(Category, on_delete=models.CASCADE)

	excerpt = models.CharField(max_length=200, blank=True)

	tag = models.ManyToManyField(Tag, blank=True)


	def __str__(self):
		return self.title

	def get_absolute_url(self):
		return reverse('detail', kwargs={'pk': self.pk})
		
	class Meta:
		ordering = ['-posted_time']

		