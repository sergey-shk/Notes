from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views

urlpatterns = [
    path('', views.index),
    path('new', views.new_note),
    path('auth', views.auth),
    path('accounts/', include('django.contrib.auth.urls')),
]
