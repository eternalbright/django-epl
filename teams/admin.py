from itertools import chain

from django.contrib import admin

from teams.models import Team


@admin.register(Team)
class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'players', 'points')

    @staticmethod
    def players(model):
        return list(model.players.all())

    @staticmethod
    def points(model):
        home_points = [x.home_points for x in model.home_matches.all()]
        guest_points = [x.guest_points for x in model.guest_matches.all()]

        return sum(home_points + guest_points)
