from rest_framework import serializers

from client.models import Client
from mailing.models import Mailing
from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Message
        fields = ('id', 'date_created', 'status', 'mailing', 'client')


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator', 'tag', 'time_zone')


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ('id', 'text', 'data_start', 'data_end', 'client_filter')


class MailingStaticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    data_start = serializers.DateTimeField()
    data_end = serializers.DateTimeField()
    messages = serializers.IntegerField()

