from rest_framework import serializers

from message.models import Message


class MessageSerializer(serializers.ModelSerializer):
    mailing = serializers.CharField(source='mailing.text')
    client = serializers.CharField(source='client.phone_number')

    class Meta:
        model = Message
        fields = ('id', 'date_created', 'status', 'mailing', 'client')
