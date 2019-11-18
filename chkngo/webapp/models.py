from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Restaurant (models.Model):
	RestaurantID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Restaurant ID")#PK
	#RMngID = models.ForeignKey(Manager, on_delete = models.CASCADE)
	#ReviewID = models.ForeignKey(Review, on_delete = models.CASCADE)
	Accommodations = models.CharField(max_length=300, default='not set')
	Seating = models.CharField(max_length=50, default='not set')
	Rating = models.IntegerField(editable = True, default = 0)

	def __str__(self):
		return str(self.RestaurantID)

class Review(models.Model):
	ReviewID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Review ID")#PK
	RestaurantID = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
	Rating = models.IntegerField(editable = True)
	Reviews = models.CharField(max_length=300, default='none')
	def __str__ (self):
		return str(self.ReviewID)
		
class TimeRecorder(models.Model):
	RestaurantID = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
	#RMngID = models.ForeignKey(Manager, on_delete = models.CASCADE)
	CurrentWaitTime = models.IntegerField(editable = True, default = 0)
	PeakWaitTime = models.IntegerField(editable = True, default = 0)
	AveWaitTime = models.IntegerField(editable = True, default = 0)
	def __str__(self):
		return str(self.RestaurantID)


