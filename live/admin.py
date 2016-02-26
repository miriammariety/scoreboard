from django.contrib import admin
from live.models import Cluster, Event, Match


class MatchInline(admin.TabularInline):
    model = Match


class EventAdmin(admin.ModelAdmin):
    inlines = [MatchInline,]
    list_display = ('name', 'location', 'start_time', 'is_major')


admin.site.register(Cluster)
admin.site.register(Event, EventAdmin)
