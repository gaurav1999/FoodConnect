from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    phone = PhoneNumberField(blank=False)
    is_supplier = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.user.username} Profile'
    