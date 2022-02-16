from celery import shared_task
from celery.utils.log import get_task_logger
from django.core import serializers
from django.core.mail import EmailMessage

from mailing.models import Mailing
from message.models import Message

logger = get_task_logger(__name__)


@shared_task()
def every_day_mail_sendler():
    """Функция для отправка статистики на почту
    """
    mails = Mailing.objects.prefetch_related('messages').filter(
        messages__status='Отправка')
    msg = []
    for mail in mails:
        msg.append({
            "title": mail.text,
            "data_start": mail.data_start,
            "data_end": mail.data_end,
            "messages": [msg for msg in mail.messages.all()]
        })

    email = EmailMessage(
        subject='Статистика по обработанным рассылкам',
        body=msg,
        from_email='from@testmail.com',
        to=['to@testmail.com'],
    )
    email.send()
