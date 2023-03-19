
from django.contrib import admin
from django.urls import path
from messenger import urls
from django.shortcuts import HttpResponse
import json
from django.contrib import admin
from django.urls import path, include
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
import requests
from .views import *

urlpatterns = [
    path('messaging-webhook/', send_response, name='token'),
]
