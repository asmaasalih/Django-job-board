from django.db import models

# Create your models here.
class Info(models.Model):
    place = models.CharField(max_length=50)
    phone_number = models.IntegerField(max_length=20)
    emai = models.EmailField( max_length=50)
        