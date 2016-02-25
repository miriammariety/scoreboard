from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'home/$', views.HomeView.as_view(), name='home')
]

