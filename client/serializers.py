from rest_framework import serializers
from taggit.serializers import TagListSerializerField, TaggitSerializer

from client.models import Client


class ClientSerializer(TaggitSerializer, serializers.ModelSerializer):
    tags = TagListSerializerField(help_text="Добавлять теги через запятую, "
                                            "в [] (прим: ['tag1', 'tag2']")

    class Meta:
        model = Client
        fields = ('id', 'phone_number', 'operator', 'tags', 'time_zone')
