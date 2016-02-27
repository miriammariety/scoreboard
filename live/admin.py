from django.contrib import admin
from live.models import Cluster, Event, Match, Rank


class MatchInline(admin.TabularInline):
    model = Match
    fields = ('left', 'right', 'winner', 'loser', 'start_time')
    readonly_fields = ('loser', )


class RankInline(admin.TabularInline):
    model = Rank
    readonly_fields = ('cluster', 'rank')


class EventAdmin(admin.ModelAdmin):
    inlines = [MatchInline, RankInline]
    list_display = ('name', 'location', 'start_time', 'is_major')

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
                            'rank', flat=True).order_by('rank').first() or 5
                        next_rank = last_rank - 1
                        loser.rankings.create(event=event, rank=next_rank)
                        if next_rank == 2:
                            match.winner.rankings.create(event=event, rank=1)

        formset.save()



admin.site.register(Cluster)
admin.site.register(Event, EventAdmin)
