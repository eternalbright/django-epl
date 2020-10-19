from django.contrib import admin

from matches.models import Goal, Match


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('id', 'match', 'player', 'minute')


@admin.register(Match)
class MatchAdmin(admin.ModelAdmin):
    list_display = ('id', 'home_team', 'guest_team', 'date')

