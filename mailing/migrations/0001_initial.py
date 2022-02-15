# Generated by Django 4.0.2 on 2022-02-15 13:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текс сообщения для доставки клиенту')),
                ('data_start', models.DateTimeField(verbose_name='Дата и время запуска рассылки')),
                ('data_end', models.DateTimeField(verbose_name='Дата и время окончания рассылки')),
                ('clients', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.client')),
            ],
        ),
    ]
