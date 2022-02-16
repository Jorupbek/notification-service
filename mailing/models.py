from django.db import models
from taggit.managers import TaggableManager

from client.models import OperatorCode


class Mailing(models.Model):
    text = models.TextField("Текс сообщения для доставки клиенту")
    data_start = models.DateTimeField('Дата и время запуска рассылки')
    data_end = models.DateTimeField('Дата и время окончания рассылки')
    operator = models.ForeignKey(OperatorCode, on_delete=models.CASCADE)
    tags = TaggableManager()

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'
