from django.db import models

from client.models import Client
from mailing.models import Mailing


SEND_STATUS = [
    ('Принято', 'Принято'),
    ('В очереди', 'В очереди'),
    ('Доставлено', 'Доставлено'),
    ('Частично доставлено', 'Частично доставлено'),
    ('Отклонено', 'Отклонено'),
]


class Message(models.Model):
    date_created = models.DateTimeField('Дата и время создания (отправки)')
    status = models.CharField(max_length=100, choices=SEND_STATUS,
                              default='В очереди',
                              verbose_name="Выбор статуса")
    mailing = models.ForeignKey(Mailing, on_delete=models.CASCADE,
                                related_name='messages')
    client = models.ForeignKey(Client, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.date_created} - {self.status}'

    class Meta:
        verbose_name = 'Сообщение'
        verbose_name_plural = 'Сообщения'
