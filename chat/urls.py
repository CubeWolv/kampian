from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('chat', views.chat, name='chat'),

]