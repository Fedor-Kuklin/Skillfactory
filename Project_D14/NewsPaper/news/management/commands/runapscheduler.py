import logging

from django.conf import settings

from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.triggers.cron import CronTrigger
from django.core.management.base import BaseCommand
from django_apscheduler.jobstores import DjangoJobStore
from django_apscheduler.models import DjangoJobExecution
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from datetime import datetime
from news.models import Post, Mail, Category

logger = logging.getLogger(__name__)


def my_job():

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


# функция которая будет удалять неактуальные задачи
def delete_old_job_executions(max_age=604_800):
    """This job deletes all apscheduler job executions older than `max_age` from the database."""
    DjangoJobExecution.objects.delete_old_job_executions(max_age)


class Command(BaseCommand):
    help = "Runs apscheduler."

    def handle(self, *args, **options):
        scheduler = BlockingScheduler(timezone=settings.TIME_ZONE)
        scheduler.add_jobstore(DjangoJobStore(), "default")

        # добавляем работу нашему задачнику
        scheduler.add_job(
            my_job,
            trigger=CronTrigger(second="*/10"),  # Тоже самое что и интервал, но задача тригера таким образом более понятна django
            id="my_job",  # уникальный айди
            max_instances=1,
            replace_existing=True,
        )
        logger.info("Added job 'my_job'.")

        scheduler.add_job(
            delete_old_job_executions,
            trigger=CronTrigger(
                day_of_week="mon", hour="00", minute="00"
            ),  # Каждую неделю будут удаляться старые задачи, которые либо не удалось выполнить, либо уже выполнять не надо.
            id="delete_old_job_executions",
            max_instances=1,
            replace_existing=True,
        )
        logger.info(
            "Added weekly job: 'delete_old_job_executions'."
        )

        try:
            logger.info("Starting scheduler...")
            scheduler.start()
        except KeyboardInterrupt:
            logger.info("Stopping scheduler...")
            scheduler.shutdown()
            logger.info("Scheduler shut down successfully!")