from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    is_inmate = models.BooleanField(default = False)
    is_official = models.BooleanField(default = False)

class Inmate(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    FName = models.CharField(max_length = 25)
    MName = models.CharField(max_length = 25)
    LName = models.CharField(max_length = 25)
    RoomNo = models.IntegerField()
    PhNo = models.CharField(max_length = 25)
    email = models.EmailField(max_length = 30)


class Staff(models.Model):
    user = models.OneToOneField(User, on_delete = models.CASCADE, primary_key = True)
    FName = models.CharField(max_length = 25)
    MName = models.CharField(max_length = 25)
    LName = models.CharField(max_length = 25)
    Role = models.CharField(max_length = 25)
    PhNo = models.CharField(max_length = 25)
    Address = models.CharField(max_length = 30)    