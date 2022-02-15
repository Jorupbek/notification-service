# Generated by Django 4.0.2 on 2022-02-15 14:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('client', '0002_alter_client_options_alter_operatorcode_options_and_more'),
        ('mailing', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mailing',
            options={'verbose_name': 'Рассылка', 'verbose_name_plural': 'Рассылки'},
        ),
        migrations.RemoveField(
            model_name='mailing',
            name='clients',
        ),
        migrations.AddField(
            model_name='mailing',
            name='clients',
            field=models.ManyToManyField(to='client.Client'),
        ),
    ]
