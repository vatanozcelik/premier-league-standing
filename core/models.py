from django.db import models
from django.utils.text import slugify


class League(models.Model):
    slug = models.SlugField(max_length=200, blank=True, null=True)
    name = models.CharField(max_length=255)
    country = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(League, self).save(*args, **kwargs)


class Team(models.Model):
    league = models.ForeignKey(
        League, blank=True, null=True, on_delete=models.CASCADE)
    image = models.ImageField(
        upload_to="images/", default='images/Wolves.png',  blank=True, null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(
        max_length=100, unique=True, null=True)
    win = models.IntegerField(blank=True, null=True)
    draw = models.IntegerField(blank=True, null=True)
    loss = models.IntegerField(blank=True, null=True)
    scored = models.IntegerField(blank=True, null=True)
    conceded = models.IntegerField(blank=True, null=True)

    games = models.IntegerField(blank=True, null=True)
    point = models.IntegerField(blank=True, null=True)
    average = models.IntegerField(blank=True, null=True)

    class Meta:
        ordering = [
            '-point', '-average'
        ]

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.games = self.win + self.draw + self.loss
        self.point = self.win*3 + self.draw
        self.average = self.scored - self.conceded
        self.slug = slugify(self.name)

        super(Team, self).save(*args, **kwargs)


class Footballer(models.Model):
    player = models.CharField(max_length=255, blank=True, null=True)
    position = models.CharField(max_length=255, blank=True, null=True)
    team = models.ForeignKey(Team, on_delete=models.CASCADE)

    def __str__(self):
        return self.player

    class Meta:
        ordering = (
            'position',
        )
