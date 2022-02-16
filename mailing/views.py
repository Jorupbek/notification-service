from rest_framework import generics, viewsets

from client.models import Client
from mailing.models import Mailing
from mailing.serializers import MailingStaticSerializer, MailingSerializer
from mailing.tasks import send_message


class MailingList(viewsets.ModelViewSet):
    serializer_class = MailingSerializer

    def perform_create(self, serializer):
        operator = serializer.validated_data.get('operator')
        serializer.save()
        send_message.delay(operator.id, serializer.instance.id)

    def get_queryset(self):
        return Mailing.objects.all()


class MailingStatistic(generics.ListAPIView):
    serializer_class = MailingStaticSerializer

    def get_queryset(self):
        mails = Mailing.objects.prefetch_related('messages').all()
        return mails
