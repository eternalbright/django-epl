from django.db import models


class Team(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ['pk']

    def __str__(self):
        return f'{self.name}'
