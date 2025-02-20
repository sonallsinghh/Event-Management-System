from django.db import models

class Category(models.Model):
	name = models.CharField(max_length=100)
	cover_image = models.ImageField(upload_to='category_covers/', null=True, blank=True)  
	
	def __str__(self):
		return self.name

class Event(models.Model):
	name = models.CharField(max_length=100)
	category = models.ForeignKey(Category, on_delete=models.CASCADE)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()
	priority = models.IntegerField(default=1)
	description = models.TextField(default='')
	location = models.CharField(max_length=255, default='')
	organizer = models.CharField(max_length=100, default='')

	# def __str__(self):
	# 	return self.name

	