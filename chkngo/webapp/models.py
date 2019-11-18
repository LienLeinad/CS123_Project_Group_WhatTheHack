from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Restaurant (models.Model):
    RestoID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Restaurant ID")#PK
    MngID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Manager ID")#PK
	ReviewID = models.ForeignKey(Review, on_delete=models.CASCADE)
	Accommodations = models.CharField(max_length=300, default='not set')
	Seating = models.CharField(max_length=50, default='not set')
	Rating = models.IntegerField(editable = True, default = 0)
	WaitTime2_4 = models.IntegerField(editable = True, default = 0)
	WaitTime5_8 = models.IntegerField(editable = True, default = 0)
	WaitTime9_10 = models.IntegerField(editable = True, default = 0)

    def __str__(self):
        return str(self.RestoID)

class Review(models.Model):
	ReviewID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Review ID")#PK
    RestoID = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    Rating = models.IntegerField(editable = True)
	ReviewDetail = models.CharField(max_length=300, default='no Reviews')
    def __str__ (self):
        return str(self.Rating)

class CustomUser(AbstractUser):
    contact = models.CharField(
        max_length = 11,
        verbose_name = 'Contact Numbers',
        default = 'n/a'
    )
    def __str__(self):
        return self.username
