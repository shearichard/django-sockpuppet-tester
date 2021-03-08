from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

urlpatterns = [
    path('increment/', increment, name='increment'),
] + staticfiles_urlpatterns()

