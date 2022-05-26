from django.db.models.signals import m2m_changed
from django.dispatch import receiver  # импортируем нужный декоратор
from .models import PostCategory, Mail, Post
from .tasks import do_mail
from django.template.loader import render_to_string
from django.core.mail import EmailMultiAlternatives


@receiver(m2m_changed, sender=PostCategory)
def do_mailing(sender, instance, action, **kwargs):

    if action == 'post_add':
        do_mail(sender, instance)
        # category_list = list(sender.objects.filter(postThrough=instance.id).values('categoryThrough'))
        #
        # for category in category_list:
        #     mail_list = list(Mail.objects.filter(category=category['categoryThrough']).values('subscribers__username',
        #                                                                                         'subscribers__email'))
        #
        #     for mail in mail_list:
        #         html_content = render_to_string(
        #             'mail.html',
        #             {
        #                 'post': instance,
        #                 'text': instance.text,
        #                 'username': mail["subscribers__username"],
        #             }
        #         )
        #         msg = EmailMultiAlternatives(
        #             subject=f'Здравствуйте, уважаемый {mail["subscribers__username"]}. Обновления статей!',
        #             from_email='kuklin.fed@yandex.ru',
        #             to=[mail['subscribers__email']],
        #         )
        #         msg.attach_alternative(html_content, "text/html")
        #
        #         msg.send()