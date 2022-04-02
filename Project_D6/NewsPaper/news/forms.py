from django import forms
from django.forms import ChoiceField, CharField, MultipleChoiceField, DateTimeField
from django.forms import ModelForm
from django.forms.widgets import Textarea, CheckboxSelectMultiple, DateTimeInput
from .models import Post, Category
from django.contrib.auth.models import User


class PostForm(ModelForm):
    def __init__(self, *args, **kwargs):
        super(PostForm, self).__init__(*args, **kwargs)
        self.fields['author'].label = 'Имя автора'

        choice = []
        for names in Category.objects.all().values('id', 'name'):
            choice.append((names.get('id'), names.get('name')))
        self.fields['postCategory'].choices = choice

    categoryType = ChoiceField(choices=Post.CATEGORY_CHOICES, label='Тип публикации')
    title = CharField(max_length=255, empty_value='Без названия', label='Заголовок')
    text = CharField(empty_value='Без содержания', label='Содержание', widget=Textarea(attrs={'cols': 100, 'rows': 4}))
    postCategory = MultipleChoiceField(label='Категории', widget=CheckboxSelectMultiple)

    class Meta:
        model = Post
        fields = ('author', 'categoryType', 'title', 'postCategory', 'text',)



class UserForm(ModelForm):

    class Meta:
        model = User
        fields = ['username',
                  'last_name',
                  'first_name',
                  'email',
                  ]

