

from django.contrib import admin
from django.urls import path
from .views import view, template
urlpatterns = [
    path('', view),
    path('template', template)
]