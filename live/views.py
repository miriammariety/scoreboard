from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView

from live.models import Event, Cluster

class HomeView(TemplateView):
    template_name = 'live/homepage.html'


class ScheduleView(ListView):
    template_name = 'live/schedule.html'
    model = Event
    context_object_name = 'event_list'

class ClusterPageView(DetailView):
    template_name = 'live/specpages/clusterpage.html'
    model = Cluster