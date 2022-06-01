from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
import django.contrib.auth
from django.core.cache import cache
from django.utils.translation import gettext as _
from django.utils.translation import pgettext_lazy


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name=_('Author_User'))
    ratingAuthor = models.SmallIntegerField(default=0, verbose_name=_('Rating Author'))

    class Meta:
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')

    def update_rating(self):
        postRarings = self.post_set.aggregate(postRating=Sum('rating'))
        pRatings = 0
        pRatings += postRarings.get('postRating')
        commentRatings = self.authorUser.comment_set.aggregate(commentRating=Sum('rating'))
        cRatings = 0
        cRatings += commentRatings.get('commentRating')

        self.ratingAuthor = pRatings * 3 + cRatings
        self.save()

    def __str__(self):
        return f'{self.authorUser}'


class Category(models.Model):
    name = models.CharField(max_length=64, unique=True, verbose_name=_('Name'), help_text=_('category name'))

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categorys')

    def __str__(self):
        return f'{self.name}'


class Mail(models.Model):
    subscribers = models.ForeignKey(django.contrib.auth.get_user_model(), on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name=_('Author'))

    NEWS = 'NW'
    ARTICLE = 'AR'
    CATEGORY_CHOICES = (
        (NEWS, _('News')),
        (ARTICLE, _('Article')),
    )
    categoryType = models.CharField(
                                    max_length=2, choices=CATEGORY_CHOICES,
                                    default=NEWS, verbose_name=_('Type category')
                                   )
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Creation'))
    postCategory = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=128, verbose_name=_('Title'))
    text = models.TextField(verbose_name=_('Text'))
    rating = models.SmallIntegerField(default=0, verbose_name=_('Rating'))

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f'{self.text[0:123]}...'

    def __str__(self):
        return f'{self.title}, {self.text[:20]}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/news/{self.id}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'news-{self.id}')  # затем удаляем его из кэша, чтобы сбросить его

    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')



class PostCategory(models.Model):
    postThrough = models.ForeignKey(Post, on_delete=models.CASCADE)
    categoryThrough = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    commentPost = models.ForeignKey(Post, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name=_('Date Creation'))
    text = models.TextField(verbose_name=_('Text'))
    rating = models.SmallIntegerField(default=0, verbose_name=_('Rating'))

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()