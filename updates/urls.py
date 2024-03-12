from django.urls import path
from . import views

urlpatterns = [
    path('updates', views.updates, name='updates'),
    path('update/<int:update_id>/', views.updatesview, name='updatesview'),
    path('addupdates', views.addupdates ,name='addupdates'),
    path('delete_update/<int:update_id>/', views.delete_update, name='delete_update'),

]