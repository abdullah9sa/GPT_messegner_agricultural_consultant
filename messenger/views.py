
from django.shortcuts import render, redirect,HttpResponse
from django.views.decorators.csrf import csrf_protect
from django.core.paginator import Paginator
from django.contrib import messages
from django.views.decorators.http import require_http_methods
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Count
from datetime import datetime


# Create your views here.
def index(request):

    return HttpResponse("Jinx")

def messaging_webhook(request):
    if request.method == 'GET':
        # Parse the query params
        mode = request.GET.get('hub.mode', '')
        token = request.GET.get('hub.verify_token', '')
        challenge = request.GET.get('hub.challenge', '')

        # Check if a token and mode is in the query string of the request
        if mode and token:
            # Check the mode and token sent is correct
            if mode == 'subscribe' and token == 'EAAKkb0lzBWEBAE073UeZCPAzFotoE3JebK4cZCnYJsDZCSVJCM76TZAXlge2AWOFgU3VAsQGvZBINDtfSlFN9ZCafq95iv4y5tuxMi6c2k5cOZCfSgO6PUEbk28mK7iqoGajBd3ZCO4YOZBujmrSup3anxAhZCKOuTGGJYbVc7rx5iscZCK1aRaEuzK':
                # Respond with the challenge token from the request
                return HttpResponse(challenge, content_type='text/plain', status=200)
            else:
                # Respond with '403 Forbidden' if verify tokens do not match
                return HttpResponse(status=403)
        else:
            # Respond with '400 Bad Request' if query params are missing
            return HttpResponse(status=403)
# def messaging_webhook(request):
#     mode = request.GET.get("hub.mode")
#     token = request.GET.get("hub.verify_token")
#     challenge = request.GET.get("hub.challenge")

#     if mode and token:
#         if mode == "subscribe":# and token == config.verifyToken:
#             print("WEBHOOK_VERIFIED")
#             return HttpResponse(challenge, status=200)
#         else:
#             return HttpResponse(status=403)
#     else:
#         return HttpResponse(status=400)