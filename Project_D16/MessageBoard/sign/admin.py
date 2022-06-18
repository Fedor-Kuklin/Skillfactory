from django.contrib import admin
from django.contrib.auth.admin import Group

from .models import OneTimeCode


admin.site.register(OneTimeCode)
admin.site.unregister(Group)
