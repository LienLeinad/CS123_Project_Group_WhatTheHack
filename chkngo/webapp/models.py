from django.db import models
from django.contrib.auth.models import User,AbstractUser
# Create your models here.

class Restaurant (models.Model):
    RestoID = models.CharField(max_length = 30, unique = True, primary_key = True, verbose_name = "Restaurant ID")#PK
    Rating = models.IntegerField(editable = True, default = 0)

    def __str__(self):
        return str(self.RestoID)

class Review(models.Model):
    RestoID = models.ForeignKey(Restaurant, on_delete = models.CASCADE)
    Rating = models.IntegerField(editable = True)
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
