from django import forms

from django.forms import ModelForm

from .models import Post


# Создаём модельную форму
class PostForm(ModelForm):
    # в класс мета, как обычно, надо написать модель, по которой будет строится форма и нужные нам поля. Мы уже делали что-то похожее с фильтрами.
    class Meta:
        model = Post
        fields = ['author', 'title', 'categoryType',  'postCategory', 'text']

        labels = {
            'author': 'Автор',
            'title': 'Название',
            'categoryType': 'Тип Категории',
            'postCategory': 'Категория',
            'text': 'Текст',

        }
        widgets ={'text': forms.Textarea(attrs={'cols': 100, 'rows': 4})

                 }

