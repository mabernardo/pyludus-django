import datetime
from django.db import models


class Platform(models.Model):
    pass


class Genre(models.Model):
    pass


class Developer(models.Model):
    pass


class Publisher(models.Model):
    pass


class Game(models.Model):
    name = models.CharField(max_length=200)
    platforms = models.ManyToManyField(Platform)
    genres = models.ManyToManyField(Genre)
    release_year = models.IntegerField(null=True)
    release_month = models.IntegerField(null=True)
    release_day = models.IntegerField(null=True)
    developer = models.OneToOneField(Developer, on_delete=models.PROTECT)
    publisher = models.OneToOneField(Publisher, on_delete=models.PROTECT)
    overview = models.TextField(null=True)
    esrb_rating = models.CharField(null=True)
    players = models.CharField(null=True)
    coop = models.BooleanField(default=False)
    rating = models.FloatField(null=True)
    location = models.CharField(null=True)
    notes = models.CharField(null=True)
    tags = models.CharField(null=True)
    finished = models.BooleanField(default=False)
    original = models.BooleanField(default=False)
    playtime = models.IntegerField(null=True)
    youtube_url = models.CharField(null=True)
    logo_url = models.CharField(null=True)
    status = models.IntegerField(null=True)
    provider = models.CharField(null=True)
    provider_id = models.CharField(null=True)
    created = models.DateTimeField(default=datetime.datetime.now())
