from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    Re_enter_email=models.EmailField
    Re_enter_password=models.CharField()
    Mobile=models.CharField()
    address=models.TextField()
