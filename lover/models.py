from django.db import models

# Create your models here.
class User(models.Model):
    phonenumer = models.CharField(max_length=20,null=True)
    name = models.CharField(max_length=30)
    gender = models.BooleanField()
    password = models.CharField(max_length=20)

