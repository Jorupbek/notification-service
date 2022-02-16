from celery import shared_task
from celery.utils.log import get_task_logger
from django.utils import timezone

from client.models import Client
from mailing.models import Mailing
from message.models import Message

logger = get_task_logger(__name__)


@shared_task
def send_message(operator, instance_id):
    """Функция для создания сообщения и отправка сообщения

    Args:
      operator: Список отфоматированных клиентов
      instance_id: id текущей рассылки

    """
    msgs = []
    now = timezone.now()
    mailing = Mailing.objects.get(id=instance_id)
    clients_list = Client.objects.filter(operator_id=operator)

    for client in clients_list:
        msgs.append(Message(date_created=now, status='Отправка',
                              mailing=mailing, client=client))
    try:
        Message.objects.bulk_create(msgs)
        logger.info("Рассылка сообщений отправлено")
    except Exception as e:
        logger.error(f"Сообщения не отправлены по причине ошибки: ", e)
