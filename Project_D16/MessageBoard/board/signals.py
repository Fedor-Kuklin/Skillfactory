from django.conf import settings
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import *


@receiver(post_save, sender=Comment)
def send_msg(instance, created, **kwargs):

    user = User.objects.get(pk=instance.commentUser_id)
    pk_response = instance.id
    if created:
        # если создан отклик, отправить сообщение автору объявления

        pk_ad = instance.commentAd_id
        user = f'{user.username}'
        user_id = Ad.objects.get(pk=pk_ad).author_id
        ad_title = Ad.objects.get(pk=pk_ad).title
        response_text = Comment.objects.get(pk=pk_response).text
        response_time = Comment.objects.get(pk=pk_response).dateCreation

        title = f'У вас новый отклик от {str(user)[:15]}'
        msg = f'На ваше объявление "{ad_title}" пришел {str(response_time)[:19]} новый отклик\n' \
              f'от {user} следующего содержания: ' \
              f'{response_text}. Перейти в отклики http://127.0.0.1:8000/ad/comment/'
        email = settings.DEFAULT_FROM_EMAIL
        ad_email = User.objects.get(pk=user_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[ad_email, ])

    elif instance.status_add:
        # если отклик принят, то автору отклика отправить письмо-уведомление

        ad_title = Ad.objects.get(pk=Comment.objects.get(pk=pk_response).commentAd_id).title
        ad_id = Ad.objects.get(pk=Comment.objects.get(pk=pk_response).commentAd_id).id
        comment_time = Comment.objects.get(pk=pk_response).dateCreation

        title = f'У вас одобренный отклик на объявление "{str(ad_title)[:15]}"'
        msg = f'На ваш отклик от {str(comment_time)[:19]} на объявление "{ad_title}" пришло положительное ' \
              f'подтверждение. Перейти на объявление http://127.0.0.1:8000/ad/{ad_id}'
        email = settings.DEFAULT_FROM_EMAIL
        comment_email = User.objects.get(pk=Comment.objects.get(pk=pk_response).commentUser_id).email

        send_mail(subject=title, message=msg, from_email=email, recipient_list=[comment_email, ])
