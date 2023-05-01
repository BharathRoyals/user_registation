from django.db import models

# Create your models here.
from django.contrib.auth.models import User
class profile(models.Model):
    Username=models.OneToOneField(User,on_delete=models.CASCADE)
    Addess=models.TextField()
    profile_pic=models.ImageField()