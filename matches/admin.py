from django.contrib import admin

from matches.models import Goal, Match


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('match', 'player', 'minute')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('home_team', 'guest_team', 'date', 'status', 'score')
    list_editable = ('status',)

    @staticmethod
    def score(model):
        return f'{model.home_score}:{model.guest_score}'
