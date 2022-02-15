from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

from api.views import api_root

schema_view = get_schema_view(
   openapi.Info(
       title="Сервис уведомлений API",
       default_version='v1'
   ),
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('docs/', schema_view.with_ui('swagger', cache_timeout=0),
         name='schema-swagger-ui'),
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),
    path('api/', api_root),
    path('mailing/', include('mailing.urls')),
    path('message/', include('mailing.urls')),
    path('client/', include('mailing.urls')),
]
