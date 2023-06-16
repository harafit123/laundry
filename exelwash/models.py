from django.db import models
from datetime import datetime
from django.contrib.auth.models import User
# Create your models here.



class Enquiry(models.Model):
    name=models.CharField(max_length=30)
    email=models.EmailField()
    message=models.TextField()
    is_resolved= models.BooleanField(default=False)
    contacted_date = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.email


class Profile(models.Model):
    user = models.OneToOneField(User , on_delete=models.CASCADE)
    auth_token = models.CharField(max_length=100 )
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username
