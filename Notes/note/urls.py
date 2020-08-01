from django.contrib import admin
from django.urls import path
from django.urls import include
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('new', views.new_note, name='new_note'),
    path('auth', views.auth),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.signup, name='signup'),
    path('edit/<int:pk>', views.edit_note, name='edit_note'),
    path('delete_note/<int:pk>', views.del_note, name='delete_note'),
]
