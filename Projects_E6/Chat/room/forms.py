from django.forms import ModelForm, TextInput

from .models import *


class RoomCreateForm(ModelForm):

    class Meta:
        model = Room
        fields = ('name', 'slug',)