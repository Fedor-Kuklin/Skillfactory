from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models


class Ad(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Author')

    TANKS = 'TN'
    HEALERS = 'HL'
    DD = 'DD'
    MERCHANTS = 'MR'
    GUILD_MASTER = 'GM'
    QUEST_GIVERS = 'QG'
    BLACKSMITHS = 'BS'
    TANNERS = 'TA'
    POTION_MAKERS = 'PM'
    SPELL_MASTERS = 'SM'
    CATEGORY_CHOICES = (
        (TANKS, 'Tanks'),
        (HEALERS, 'Healers'),
        (DD, 'DD'),
        (MERCHANTS, 'Merchants'),
        (GUILD_MASTER, 'Guild Masters'),
        (QUEST_GIVERS, 'Quest Givers'),
        (BLACKSMITHS, 'Blacksmiths'),
        (TANNERS, 'Tanners'),
        (POTION_MAKERS, 'Potion Makers'),
        (SPELL_MASTERS, 'Spell Masters'),
    )
    categoryType = models.CharField(
                                    max_length=2, choices=CATEGORY_CHOICES,
                                    default=TANKS, verbose_name='Type category'
                                   )
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')
    title = models.CharField(max_length=128, verbose_name='Title')
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.author}'

    def get_absolute_url(self):  # добавим абсолютный путь, чтобы после создания нас перебрасывало на страницу с товаром
        return f'/ad/{self.id}'

    class Meta:
        ordering = ('-dateCreation',)
        verbose_name = 'Ad'
        verbose_name_plural = 'Ads'


class Comment(models.Model):
    commentAd = models.ForeignKey(Ad, on_delete=models.CASCADE)
    commentUser = models.ForeignKey(User, on_delete=models.CASCADE)
    dateCreation = models.DateTimeField(auto_now_add=True, verbose_name='Date Creation')
    text = models.TextField(verbose_name='Text')
    status_remove = models.BooleanField(default=False, verbose_name='Отклик - отклонен')
    status_add = models.BooleanField(default=False, verbose_name='Отклик - принят')

    class Meta:
        ordering = ('-dateCreation',)
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

