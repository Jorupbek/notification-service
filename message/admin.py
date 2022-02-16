from django.contrib import admin
from message.models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['date_created', 'mailing', 'client', 'status']
    list_display_links = ['date_created', 'mailing', 'client', 'status']
