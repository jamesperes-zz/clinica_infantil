from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views


urlpatterns = [
    path('', views.home, name="home"),
    path('sistema', views.sistema, name="sistema_home"),
]
