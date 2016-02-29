import collections

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

    def get_context_data(self, **kwargs):
        context = super(ScheduleView, self).get_context_data(**kwargs)
        context['major_events'] = self.get_major()
        context['minor_events'] = self.get_minor()
        context['special_events'] = self.get_special()
        return context

    def get_major(self):
        return Event.objects.filter(is_major=True).filter(
            matches__isnull=False).distinct()

    def get_minor(self):
        return Event.objects.filter(is_major=False).filter(
                matches__isnull=False).distinct()

    def get_special(self):
        return Event.objects.filter(matches__isnull=True).distinct()


class ClusterPageView(DetailView):
    template_name = 'live/specpages/clusterpage.html'
    model = Cluster
    context_object_name = 'cluster'

    def get_context_data(self, **kwargs):
        context = super(ClusterPageView, self).get_context_data(**kwargs)
        events = self.get_events()
        event_stat = {}

        for event in events:
            win = event.matches.filter(winner=self.object).count()
            loss = event.matches.filter(loser=self.object).count()

            try:
                rank = event.rankings.get(cluster=self.object).rank
            except Rank.DoesNotExist:
                rank = "--"

            event_stat[event] = ( win, loss, rank )

        context['event_stat'] = event_stat

        return context

    def get_events(self):
        return Event.objects.filter(Q(matches__left=self.object)|Q(matches__right=self.object))


class ScoreboardView(ListView):
    template_name = 'live/scoreboard.html'
    model = Event
    context_object_name = 'events'
    ordering = ('name', )

    def get_context_data(self, **kwargs):
        context = super(ScoreboardView, self).get_context_data(**kwargs)
        ranks = Rank.objects.all()
        events = context['events']

        scores = {}
        for event in events:
            scores[event] = ranks.filter(event=event).order_by(
                'cluster__team_name')

        scores = collections.OrderedDict(sorted(scores.items()))
        context['event_scores'] = scores
        return context

