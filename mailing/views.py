from django.utils import timezone
from rest_framework import generics, viewsets

from client.models import Client
from mailing.models import Mailing
from mailing.serializers import MailingStaticSerializer, MailingSerializer
from message.models import Message


class MailingList(viewsets.ModelViewSet):
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        operator = serializer.validated_data.get('operator')
        clients_list = Client.objects.filter(operator=operator)
        serializer.save()
        send_message(clients_list, serializer.instance)

    def get_queryset(self):
        return Mailing.objects.all()


class MailingStatistic(generics.ListAPIView):
    serializer_class = MailingStaticSerializer

    def get_queryset(self):
        mails = Mailing.objects.prefetch_related('messages').all()
        return mails


def send_message(clients_list, instance):
    """Функция для создания сообщения и отправка сообщения

    Args:
      clients_list: Список отфоматированных клиентов
      instance: Текущая рассылка

    """
    now = timezone.now()
    msgs = []

    if instance.data_start < now < instance.data_end:
        for client in clients_list:
            msgs.append(Message(date_created=now, status='Отправка',
                                  mailing=instance, client=client))

    Message.objects.bulk_create(msgs)
