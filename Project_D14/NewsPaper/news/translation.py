
from .models import Post, PostCategory, Author, Category, Comment
from modeltranslation.translator import register, \
    TranslationOptions  # импортируем декоратор для перевода и класс настроек, от которого будем наследоваться

# регистрируем наши модели для перевода

@register(Post)
class PostTranslationOptions(TranslationOptions):
    fields = ('categoryType', 'title', 'text', ) # указываем, какие именно поля надо переводить в виде кортежа


@register(Category)
class CategoryTranslationOptions(TranslationOptions):
    fields = ('name', )


