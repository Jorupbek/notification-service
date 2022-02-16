from rest_framework import serializers

from client.models import Client
from mailing.models import Mailing
from message.serializers import MessageSerializer


class MailingSerializer(serializers.ModelSerializer):
    tags = serializers.PrimaryKeyRelatedField(queryset=Client.tags.all(),
                                              many=True)

    class Meta:
        model = Mailing
        fields = ('id', 'text', 'data_start', 'data_end', 'operator', 'tags')


class MailingStaticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    data_start = serializers.DateTimeField()
    data_end = serializers.DateTimeField()
    messages = MessageSerializer(many=True)

