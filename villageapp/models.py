from django.db import models

# Create your models here.
class Panchayath(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    country = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    district = models.CharField(max_length=100)
    pincode = models.CharField(max_length=100)

    def __str__(self):
        return self.name