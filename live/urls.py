from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'schedule/$', views.ScheduleView.as_view(), name='schedule'),
    url(r'cluster/(?P<pk>\w+)$', views.ClusterPageView.as_view(), name='cluster'),
]

