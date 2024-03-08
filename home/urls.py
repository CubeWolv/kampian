from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/signup', views.signup, name='signup'),
    path('accounts/login', views.login, name='login'),
    path('aboutus', views.aboutus, name='about'),
    path('termsofuse', views.termsofuse, name='termsofuse'),
    path('contact', views.contact, name='contact'),
    path('logout/', views.custom_logout, name='logout'),
    path('pdfs/', views.pdfview, name='pdfview'),
    path('videos/', views.video, name='video'),

]