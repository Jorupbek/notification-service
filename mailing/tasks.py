from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone

from client.models import Client
from mailing.models import Mailing
from message.models import Message

logger = get_task_logger(__name__)


@shared_task
def send_message(operator, instance):
    """Функция для создания сообщения и отправка сообщения

    Args:
      operator: Список отфоматированных клиентов
      instance: Текущая рассылка

    """
    now = timezone.now()
    msgs = []
    mailing = Mailing.objects.get(id=instance)
    clients_list = Client.objects.filter(operator_id=operator)
    if mailing.data_start < now < mailing.data_end:
        for client in clients_list:
            msgs.append(Message(date_created=now, status='Отправка',
                                  mailing=mailing, client=client))

    Message.objects.bulk_create(msgs)
    logger.info("Рассылка сообщений отправлено")
