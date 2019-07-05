from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from datetime import *
from django.utils import *
# Create your models here.

class Category(models.Model):
	TYPES = (
		('CAT', 'Category'),
		('CUS', 'Cuisines'),
		('SPE', 'Special Occasions')
	)
	name = models.CharField(max_length=50, unique=True)
	type = models.CharField(max_length=25, choices=TYPES)
	likes = models.IntegerField(default=0)
	slug = models.SlugField(unique=True)
	supercat = models.ForeignKey('self', null=True, related_name='category')
	photo = models.ImageField(upload_to='cat_pics', blank=True)

	def save(self, *args, **kwargs):
		self.slug = slugify(self.name)
		super(Category, self).save(*args, **kwargs)

	class Meta:
		verbose_name_plural = 'Categories'

	def __str__(self):
		return self.name

class Chef(models.Model):
	user = models.OneToOneField(User)
	photo = models.ImageField(upload_to='profile_pics', default='profile_pics/anon.png')
	bio = models.TextField(default="Hello! I enjoy the opportunity to upload entries, create reminders, and plan ahead on this website!", blank=True)

	def __str__(self):
		return self.user.username

class Entry(models.Model):
	chef = models.ForeignKey(User)
	slug = models.SlugField(unique=True)
	categories = models.ManyToManyField(Category)
	name = models.CharField(max_length=128, unique=True)
	photo = models.ImageField(upload_to='food_pics')
	cook_time = models.IntegerField(default=0)
	date_posted = models.DateTimeField(default=timezone.now)
	ingredients = models.TextField(default="")
	steps = models.TextField(default="")
	about = models.TextField(default="Check out my new entry!")
	#overall rating

	def save(self, *args, **kwargs):
		self.slug = slugify(self.chef.username+"-"+self.name)
		super(Entry, self).save(*args, **kwargs)

	def __str__(self):
		return self.name

class Review(models.Model):
	entry = models.ForeignKey(Entry)
	author = models.ForeignKey(User)
	title = models.CharField(max_length=50, default="My Rating")
	rating = models.DecimalField(decimal_places=2,max_digits=3,default=5.00)
	comment = models.TextField(default="")
	date_posted = models.DateTimeField(default=timezone.now)

class Suggestion(models.Model):
	author = models.ForeignKey(User)
	comment = models.TextField(default="I love this website!")

class Contact(models.Model):
	first_name = models.CharField(max_length=50)
	email = models.EmailField(unique=True)
	comment = models.TextField(default="I love this website!")
