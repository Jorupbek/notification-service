from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import MessageList, ClientList, MailingList, MailingStatistic

router = SimpleRouter()

router.register('messages', MessageList, 'messages')
router.register('client', ClientList, 'client')
router.register('mailing', MailingList, 'mailing')

urlpatterns = [
    path('', include(router.urls)),
    path('stat/', MailingStatistic.as_view(), name='statistic'),
]
