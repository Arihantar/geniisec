from django.db import models

# Create your models here.

class UserInfo(models.Model):
    email = models.EmailField()
    country = models.CharField(max_length=30)
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=60)
