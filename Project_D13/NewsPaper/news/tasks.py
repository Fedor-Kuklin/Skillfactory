from celery import shared_task

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from news.models import Post, Mail, Category


@shared_task
def do_mail(sender, instance):
    category_list = list(sender.objects.filter(postThrough=instance.id).values('categoryThrough'))

    for category in category_list:
        mail_list = list(Mail.objects.filter(category=category['categoryThrough']).values('subscribers__username',
                                                                                          'subscribers__email'))

        for mail in mail_list:
            html_content = render_to_string(
                'mail.html',
                {
                    'post': instance,
                    'text': instance.text,
                    'username': mail["subscribers__username"],
                }
            )
            msg = EmailMultiAlternatives(
                subject=f'Здравствуйте, уважаемый {mail["subscribers__username"]}. Добавлена новость!',
                from_email='kuklin.fed@yandex.ru',
                to=[mail['subscribers__email']],
            )
            msg.attach_alternative(html_content, "text/html")
            msg.send()


@shared_task
def send_mailing_task():

    for category in Category.objects.all():
        news_from_each_category = []
        news =[]
        week_number_last = datetime.now().isocalendar()[1] - 2
        print(week_number_last)

        for one_news in Post.objects.filter(postCategory=category.id,
                                        dateCreation__week=week_number_last,
                                        ).values('pk',
                                                'title',
                                                'text',
                                                'dateCreation',
                                                'postCategory__name'):
            news.append(one_news)
            news_from_each_category.append(one_news.get("pk"))

        if news_from_each_category:
            mail_list = list(Mail.objects.filter(category=category.id).values('subscribers__username',
                                                                                'subscribers__email'))

            for mail in mail_list:
                html_content = render_to_string(
                    'mails.html',
                        {'data': news,
                        'category_name': category.name,
                        'user': mail['subscribers__username'],
                        'week_number_last': week_number_last,
                    }
                )
                msg = EmailMultiAlternatives(
                    subject=f'Здравствуйте, уважаемый {mail["subscribers__username"]}. Ознакомтесь с новыми статьями!',
                    from_email='kuklin.fed@yandex.ru',
                    to=[mail['subscribers__email']],
                )
                msg.attach_alternative(html_content, "text/html")
                msg.send()
