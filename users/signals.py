#Post signal emitted when any creation takes place in the db
from django.db.models.signals import post_save
#User model will be sending the signal here
from django.contrib.auth.models import User
from django.dispatch import receiver 
from .models import Profile

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()
