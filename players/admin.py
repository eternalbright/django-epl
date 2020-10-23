from django.contrib import admin

from players.models import Player


@admin.register(Player)
class PlayerAdmin(admin.ModelAdmin):
    list_display = ('name', 'team', 'matches', 'goals')

    @staticmethod
    def matches(model):
        return list(model.team.home_matches.all() | model.team.guest_matches.all())

    @staticmethod
    def goals(model):
        return len(model.goals.all())
