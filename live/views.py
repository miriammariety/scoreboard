from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from live.models import Event

class HomeView(TemplateView):
    template_name = 'live/homepage.html'

    # def get_context_data(self, **kwargs):
    #     context = super(HomeView, self).get_context_data(**kwargs)
    #     context['upcoming_events'] = Event.objects.get_upcoming()
    #     context['ongoing_events'] = Event.objects.get_current()
    #     return context


class ScheduleView(ListView):
    template_name = 'live/schedule.html'
    model = Event
    context_object_name = 'event_list'
