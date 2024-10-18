
from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    agreement = models.BooleanField(default=False)
    city = models.CharField(max_length=100)
    cnic = models.CharField(max_length=15)
    comment = models.TextField()
    dob = models.DateField()
    gender = models.CharField(max_length=10)
    hobby = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    postalCode = models.CharField(max_length=10)

    def __str__(self):
        return self.user.username