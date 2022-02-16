from django.db import models
from taggit.managers import TaggableManager


class Client(models.Model):
    phone_number = models.CharField('Номер телефона клиента',
                                    help_text='7XXXXXXXX (X - цифра от 0 до 9',
                                    max_length=150
                                    )
    operator = models.ForeignKey('OperatorCode', on_delete=models.CASCADE)
    tags = TaggableManager()
    time_zone = models.ForeignKey('TimeZone', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.operator} {self.phone_number}'

    class Meta:
        verbose_name = 'Клиент'
        verbose_name_plural = 'Клиенты'


class TimeZone(models.Model):
    time_zone = models.CharField('Часовой пояс', max_length=50)
    time_city = models.CharField('Город', max_length=200)

    def __str__(self):
        return f'{self.time_city}: {self.time_zone}'

    class Meta:
        verbose_name = 'Часовой пояс'
        verbose_name_plural = 'Часовой пояс'


class OperatorCode(models.Model):
    code = models.CharField('Код оператора', max_length=50)
    code_city = models.CharField('Имя оператора', max_length=200)

    def __str__(self):
        return f'{self.code_city}: {self.code}'

    class Meta:
        verbose_name = 'Код оператора'
        verbose_name_plural = 'Код оператора'
