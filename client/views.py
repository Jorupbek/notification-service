from rest_framework import viewsets

from client.models import Client
from client.serializers import ClientSerializer


class ClientList(viewsets.ModelViewSet):
    serializer_class = ClientSerializer

    def get_queryset(self):
        return Client.objects.all()
