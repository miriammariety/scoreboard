from django.contrib import admin
from live.models import Cluster, Event, Schedule


class ScoreInline(admin.TabularInline):
    model = Event.clusters.through
    fields = ['cluster', 'place']


class ScheduleInline(admin.TabularInline):
    model = Schedule
    fields = ['time']


class EventAdmin(admin.ModelAdmin):
    inlines = [ScoreInline, ScheduleInline]
    list_display = ('name', 'location', 'is_major', 'is_done')

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)

    def save_formset(self, request, form, formset, change):
        for form in formset:
            if getattr(form.instance, 'cluster_id', False):
                form.instance.save()
        formset.save()


admin.site.register(Cluster)
admin.site.register(Event, EventAdmin)
