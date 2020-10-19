from django.db import models

from players.models import Player
from teams.models import Team


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_teams', on_delete=models.CASCADE)
    guest_team = models.ForeignKey(Team, related_name='guest_teams', on_delete=models.CASCADE)
    date = models.DateField()

    class Meta:
        verbose_name_plural = "matches"


class Goal(models.Model):
    player = models.ForeignKey(Player, related_name='goals', on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='goals', on_delete=models.CASCADE)
    minute = models.TimeField()
