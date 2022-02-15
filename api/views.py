from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'Сообщения': reverse('messages-list', request=request, format=format),
        'Клиенты': reverse('client-list', request=request, format=format),
        'Рассылки': reverse('mailing-list', request=request, format=format),
        'Статистика': reverse('statistic', request=request, format=format),
    })
