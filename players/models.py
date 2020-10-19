from django.db import models

from teams.models import Team


class Player(models.Model):
    name = models.CharField(max_length=255)
    team = models.ForeignKey(Team, related_name='players', on_delete=models.CASCADE)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'
