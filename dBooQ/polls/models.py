from __future__ import unicode_literals
from django.contrib.auth.models import User, Permission
from django.db import models
from datetime import datetime 
from django.utils import timezone

# Create your models here.

class Tag(models.Model):
	name = models.CharField(max_length=100)

class Book(models.Model):
	tags = models.ManyToManyField(Tag)
	name = models.CharField(max_length=100)
	authorFName = models.CharField(max_length=20)
	authorLName = models.CharField(max_length=20)
	insertedDate = models.DateTimeField(auto_now_add=True)
	publishedYear = models.IntegerField(blank=True, null=True)
	firstPublishedYear = models.IntegerField(blank=True, null=True)
	pages = models.IntegerField(blank=True, null=True)


class Library(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)
	ogoh = models.BooleanField()
	avah = models.BooleanField()
