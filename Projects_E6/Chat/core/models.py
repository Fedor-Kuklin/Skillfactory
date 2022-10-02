from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db import models
from django.conf import settings


class Profile (models.Model):
    user = models.OneToOneField(User, null=True, on_delete=models.CASCADE, related_name='profile')
    status = models.BooleanField(default=False)
    profile_pic = models.ImageField(null=True, blank=True, default='user.jpg', upload_to="images/profile/")

    def __str__(self):
        return f'{self.user.username}'
