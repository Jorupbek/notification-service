from django.utils import timezone
from rest_framework import generics, viewsets

from mailing.models import Mailing
from mailing.serializers import MailingStaticSerializer, MailingSerializer
from mailing.tasks import send_message
from message.tasks import every_day_mail_sendler


class MailingList(viewsets.ModelViewSet):
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        every_day_mail_sendler()
        now = timezone.now()
        serializer.save()
        operator = serializer.validated_data.get('operator')
        mailing = Mailing.objects.get(id=serializer.instance.id)

        if mailing.data_start < now < mailing.data_end:
            send_message.delay(operator.id, serializer.instance.id)
        else:
            send_message.apply_async((operator.id, serializer.instance.id),
                                     eta=mailing.data_start)

    def get_queryset(self):
        return Mailing.objects.all()


class MailingStatistic(generics.ListAPIView):
    serializer_class = MailingStaticSerializer

    def get_queryset(self):
        mails = Mailing.objects.prefetch_related('messages').all()
        return mails
