from django.db import models
from django.contrib.auth.models import AbstractUser
class addUsers(models.Model):
    
    first_name = models.TextField(max_length=50, blank=False)
    last_name = models.TextField(max_length=50, blank=True)
    username = models.TextField(max_length=25, blank=False,unique=True)
    email = models.EmailField(max_length=50, blank=False)

    password = models.TextField(max_length=15, blank=False)


class NewUserModel(AbstractUser):
    
    sponsor = models.CharField(max_length=32,null=True)
    
    
    