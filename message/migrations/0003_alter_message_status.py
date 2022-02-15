# Generated by Django 4.0.2 on 2022-02-15 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('message', '0002_alter_message_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('Принято', 'Принято'), ('В очереди', 'В очереди'), ('Доставлено', 'Доставлено'), ('Частично доставлено', 'Частично доставлено'), ('Отклонено', 'Отклонено')], default='В очереди', max_length=100, verbose_name='Выбор статуса'),
        ),
    ]