from rest_framework import serializers

from mailing.models import Mailing
from message.serializers import MessageSerializer


class MailingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mailing
        fields = ('id', 'text', 'data_start', 'data_end', 'operator')


class MailingStaticSerializer(serializers.Serializer):
    id = serializers.IntegerField()
    text = serializers.CharField()
    data_start = serializers.DateTimeField()
    data_end = serializers.DateTimeField()
    messages = MessageSerializer(many=True)

