from django.contrib import admin
from live.models import Cluster, Event


class ScoreInline(admin.TabularInline):
    model = Event.clusters.through
    fields = ['cluster', 'place']


class EventAdmin(admin.ModelAdmin):
    inlines = [ScoreInline]
    list_display = ('name', 'location', 'begin_time', 'is_major', 'is_done')

    def save_related(self, request, form, formsets, change):
        form.save_m2m()
        for formset in formsets:
            self.save_formset(request, form, formset, change=change)

    def save_formset(self, request, form, formset, change):
        for form in formset:
            if form.instance.cluster_id:
                form.instance.save()
        formset.save()


admin.site.register(Cluster)
admin.site.register(Event, EventAdmin)
