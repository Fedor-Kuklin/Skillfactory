from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver

from .models import Room


@receiver(post_save, sender=Room)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()