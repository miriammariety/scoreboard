from . import views
from django.conf.urls import url
from django.contrib import admin

urlpatterns = [
    url(r'home/$', views.HomeView.as_view(), name='home'),
    url(r'schedule/$', views.ScheduleView.as_view(), name='schedule'),
    url(r'scoreboard/$', views.ScoreboardView.as_view(), name='scoreboard'),
    url(r'^cluster/(?P<pk>\w+)$', views.ClusterPageView.as_view(), name='cluster'),
]

