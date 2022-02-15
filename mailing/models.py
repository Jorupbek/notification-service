from django.db import models

from client.models import OperatorCode


class Mailing(models.Model):
    text = models.TextField("Текс сообщения для доставки клиенту")
    data_start = models.DateTimeField('Дата и время запуска рассылки')
    data_end = models.DateTimeField('Дата и время окончания рассылки')
    client_filter = models.ForeignKey('ClientFilter', on_delete=models.CASCADE)

    def __str__(self):
        return self.text

    class Meta:
        verbose_name = 'Рассылка'
        verbose_name_plural = 'Рассылки'


class ClientFilter(models.Model):
    name = models.CharField('Название', max_length=200)
    operator = models.ForeignKey(OperatorCode, on_delete=models.CASCADE)
    tag = models.CharField('Тег (произвольная метка)', max_length=100)

    def __str__(self):
        return self.name
