
from django.contrib import admin
from django.urls import path
from messenger import urls
from django.urls import include, re_path


urlpatterns = [
    path('', include('messenger.urls')),
    path('admin/', admin.site.urls),

]
