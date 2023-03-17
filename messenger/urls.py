
from django.contrib import admin
from django.urls import path
from messenger import urls
from .views import *

urlpatterns = [
    path('', index, name='main'),
    path('messaging-webhook/', messaging_webhook, name='token'),
]
