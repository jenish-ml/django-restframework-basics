from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=100)

    def __str__(self):
        return self.team_name


class User(models.Model):
    team = models.ForeignKey(Team, on_delete=models.CASCADE, null=True, blank=True)
    name = models.CharField(max_length=100)
    place = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name