from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    GENDER = (
        ('Male','Male'),
        ('Female','Female'),
        ('Others','Others'),
    )
    Gender = models.CharField(choices=GENDER, max_length=10)
    Phone = models.CharField(max_length=20)
    Birth_Date = models.DateField()
    Address = models.TextField()


    def __str__(self) -> str:
        return str(self.user)