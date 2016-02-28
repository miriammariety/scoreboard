from django.shortcuts import render
from django.views.generic import TemplateView, ListView, DetailView
from django.utils import timezone
from .models import Match
from django.db.models import Q

from live.models import Event, Cluster, Rank

class HomeView(TemplateView):
    template_name = 'live/homepage.html'

    def get_context_data(self, **kwargs):
        context = super(HomeView, self).get_context_data(**kwargs)
        context['ongoing_games'] = self.get_ongoing()
        context['upcoming_games'] = self.get_upcoming()
        context['recent_games'] = self.get_recent()
        return context

    def get_ongoing(self):
        return Match.objects.filter(start_time__lte=timezone.now()).filter(winner__isnull=True)

    def get_upcoming(self):
        return Match.objects.filter(start_time__gt=timezone.now()).filter(winner__isnull=True)

    def get_recent(self):
        return Match.objects.filter(start_time__lt=timezone.now()).filter(winner__isnull=False)

class ScheduleView(ListView):
    template_name = 'live/schedule.html'
    model = Event
    context_object_name = 'event_list'

class ClusterPageView(DetailView):
    template_name = 'live/specpages/clusterpage.html'
    model = Cluster

class ScoreboardView(ListView):
    template_name = 'live/scoreboard.html'
    model = Event
    context_object_name = 'event_list'



