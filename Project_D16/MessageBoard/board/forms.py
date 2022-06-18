from django.forms import ModelForm, TextInput

from .models import *


class AdUpdateForm(ModelForm):
    exclude = ['author']

    class Meta:
        model = Ad
        fields = ('categoryType', 'title','content')


class AdCreateForm(ModelForm):
    exclude = ['author']

    class Meta:
        model = Ad
        fields = ('categoryType', 'title','content')


class CommentForm(ModelForm):

    class Meta:
        model = Comment
        fields = ('text', )
        widgets = {'text': TextInput(attrs={'size': 50, 'placeholder': 'Введите комментарий'})}