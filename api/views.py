from collections import defaultdict

from django.db.models import Sum
from rest_framework import viewsets, permissions, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

from api.serializers import MessageSerializer, ClientSerializer, \
    MailingSerializer, MailingStaticSerializer
from client.models import Client
from mailing.models import Mailing
from message.models import Message


class MessageList(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()


class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()


class MailingList(viewsets.ModelViewSet):
    serializer_class = MailingSerializer

    def get_queryset(self):
        return Mailing.objects.all()


class MailingStatistic(generics.ListAPIView):
    serializer_class = MailingStaticSerializer

    def get_queryset(self):
        m_stat = defaultdict()
        mails = Mailing.objects.prefetch_related('messages').all().annotate(
            msgs_cnt=Sum('messages')).values('id', 'text', 'data_start',
                                             'data_end', 'messages')
        return list(mails)


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'messages': reverse('messages-list', request=request, format=format),
        'clients': reverse('client-list', request=request, format=format),
        'mailing lst': reverse('mailing-list', request=request, format=format),
    })
