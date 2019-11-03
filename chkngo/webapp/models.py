from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
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