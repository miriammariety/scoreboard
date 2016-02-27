from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from live.models import Event

class HomeView(TemplateView):
    template_name = 'live/homepage.html'


class ScheduleView(ListView):
    template_name = 'live/schedule.html'
    model = Event
    context_object_name = 'event_list'

