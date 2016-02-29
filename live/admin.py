from django.contrib import admin
from live.models import Cluster, Event, Match, Rank


class MatchInline(admin.TabularInline):
    model = Match
    fields = ('left', 'right', 'winner', 'loser', 'start_time')
    readonly_fields = ('loser', )


class RankInline(admin.TabularInline):
    model = Rank


class EventAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('name', )}
    inlines = [MatchInline, RankInline]
    list_display = ('name', 'location', 'start_time', 'is_major')

    def save_model(self, request, obj, form, change):
        if not obj.rankings.exists():
            cluster_rank = [Rank(cluster=cluster, event=obj) for cluster in Cluster.objects.all()]
            obj.rankings.bulk_create(cluster_rank)
        obj.save()

    def save_formset(self, request, form, formset, change):
        for matchform in formset:
            if matchform.cleaned_data.get('winner', False) and \
                matchform.has_changed():
                    # check for eliminations
                    match = matchform.instance
                    if match.winner == match.left:
                        loser = match.right
                    else:
                        loser = match.left
                    match.loser = loser
                    event = match.event
                    # check if the loser has lost before
                    if event.matches.filter(loser=loser).exists():
                        last_rank = event.rankings.values_list(
                            'rank', flat=True).order_by('-rank').first() or \
                            Cluster.objects.count() + 1
                        next_rank = last_rank - 1
                        rank_obj = loser.rankings.get(event=event)
                        rank_obj.rank = next_rank
                        rank_obj.save()
                        if next_rank == 2:
                            rank_obj = match.winner.rankings.get(event=event)
                            rank_obj.rank = 1
                            rank_obj.save()

        formset.save()


class ClusterAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('team_name', )}


admin.site.register(Cluster, ClusterAdmin)
admin.site.register(Event, EventAdmin)
