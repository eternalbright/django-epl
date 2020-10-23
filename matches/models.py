from django.db import models

from players.models import Player
from teams.models import Team


TYPES_CHOICES = (
    ('scheduling', 'scheduling'),
    ('active', 'active'),
    ('finished', 'finished'),
)


def calculate_points(score1, score2):
    points = 0

    if score1 > score2:
        points = 3
    elif score1 == score2:
        points = 1

    return points


class Match(models.Model):
    home_team = models.ForeignKey(Team, related_name='home_matches', on_delete=models.CASCADE)
    guest_team = models.ForeignKey(Team, related_name='guest_matches', on_delete=models.CASCADE)
    date = models.DateField()
    status = models.CharField(choices=TYPES_CHOICES, default=TYPES_CHOICES[0][0], max_length=10)

    @property
    def home_score(self):
        home_players = self.home_team.players.all()
        return len(self.goals.filter(player__in=home_players))

    @property
    def guest_score(self):
        guest_players = self.guest_team.players.all()
        return len(self.goals.filter(player__in=guest_players))

    @property
    def home_points(self):
        return calculate_points(self.home_score, self.guest_score) if self.status == 'finished' else 0

    @property
    def guest_points(self):
        return calculate_points(self.guest_score, self.home_score) if self.status == 'finished' else 0

    class Meta:
        ordering = ['-date']
        verbose_name_plural = 'matches'

    def __str__(self):
        return f'{self.home_team} - {self.guest_team} ({self.date})'


class Goal(models.Model):
    player = models.ForeignKey(Player, related_name='goals', on_delete=models.CASCADE)
    match = models.ForeignKey(Match, related_name='goals', on_delete=models.CASCADE)
    minute = models.DurationField()

    class Meta:
        ordering = ['pk']
