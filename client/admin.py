from django.contrib import admin
from client.models import Client, TimeZone, OperatorCode


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['operator', 'phone_number']
    list_display_links = ['operator', 'phone_number']
    list_filter = ('phone_number',)


@admin.register(TimeZone)
class TimeZone(admin.ModelAdmin):
    list_display = ['time_city', 'time_zone']
    list_display_links = ['time_city', 'time_zone']
    list_filter = ['time_zone']


@admin.register(OperatorCode)
class TimeZone(admin.ModelAdmin):
    list_display = ['code_city', 'code']
    list_display_links = ['code_city', 'code']
