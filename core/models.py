from django.db import models

class Team(models.Model):
    name = models.CharField(max_length=255)
    founded = models.CharField(max_length=255, blank=True, null=True)
