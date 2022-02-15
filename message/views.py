from rest_framework import viewsets

from message.models import Message
from message.serializers import MessageSerializer


class MessageList(viewsets.ModelViewSet):
    serializer_class = MessageSerializer

    def get_queryset(self):
        return Message.objects.all()
