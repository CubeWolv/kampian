from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('signup', views.signup, name='signup'),
    path('login', views.login, name='login'),
    path('aboutus', views.aboutus, name='about'),
    path('termsofuse', views.termsofuse, name='termsofuse'),
    path('contact', views.contact, name='contact'),
    path('logout/', LogoutView.as_view(next_page='home'), name='logout'),

]
