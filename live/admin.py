from django.contrib import admin
from live.models import Cluster, Event


class ScoreInline(admin.TabularInline):
    model = Event.clusters.through
    fields = ['cluster', 'points']


class EventAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    list_display = ('name', 'location', 'begin_time', 'is_major', 'is_done')


admin.site.register(Cluster)
admin.site.register(Event, EventAdmin)
