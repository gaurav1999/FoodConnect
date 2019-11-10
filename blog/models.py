from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    pincode = models.CharField(default="000000",max_length=6)
    address_vendor = models.CharField(default= "Unknown", max_length=100)
    created_on = models.DateTimeField(auto_now_add=True)
    is_veg = models.BooleanField(default=True)

    def __str__(self):
        return self.title