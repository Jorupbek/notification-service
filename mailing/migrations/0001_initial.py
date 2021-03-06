# Generated by Django 4.0.2 on 2022-02-16 18:56

from django.db import migrations, models
import django.db.models.deletion
import taggit.managers


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
        ('taggit', '0004_alter_taggeditem_content_type_alter_taggeditem_tag'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(verbose_name='Текс сообщения для доставки клиенту')),
                ('data_start', models.DateTimeField(verbose_name='Дата и время запуска рассылки')),
                ('data_end', models.DateTimeField(verbose_name='Дата и время окончания рассылки')),
                ('operator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.operatorcode')),
                ('tags', taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags')),
            ],
            options={
                'verbose_name': 'Рассылка',
                'verbose_name_plural': 'Рассылки',
            },
        ),
    ]
