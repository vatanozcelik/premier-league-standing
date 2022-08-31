from django.db import models

class League(models.Model):
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    founded = models.DateField()


class Team(models.Model):
    name = models.CharField(max_length=255)
    founded = models.DateField(blank=True, null=True)
    league = models.ForeignKey(League, blank=True, null=True, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class Footballer(models.Model):
    name = models.CharField(max_length=255)
    age = models.IntegerField()
    old_club = models.CharField(max_length=255)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


