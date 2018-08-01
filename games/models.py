from django.conf import settings
from django.db import models


class Platform(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'platform'


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'genre'


class Developer(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'developer'


class Publisher(models.Model):
    name = models.CharField(max_length=200)
    website = models.URLField(null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'publisher'


class ErsbRating:
    EVERYONE = 'E'
    EVERYONE10 = 'E10'
    TEEN = 'T'
    MATURE = 'M'
    ADULTS = 'A'
    RATING_PENDING = 'RP'

    CATEGORIES = (
        (EVERYONE, 'EVERYONE'),
        (EVERYONE10, 'EVERYONE 10+'),
        (TEEN, 'TEEN'),
        (MATURE, 'MATURE'),
        (ADULTS, 'ADULTS'),
        (RATING_PENDING, 'RATING PENDING'),
    )


class Store:
    BLIZZARD = 'BLIZZARD'
    HUMBLE_BUNDLE = 'HUMBLE_BUNDLE'
    GOG = 'GOG'
    ORIGIN = 'ORIGIN'
    PSN = 'PSN'
    STEAM = 'STEAM'
    OTHER = 'OTHER'

    SUPPORTED = (
        (BLIZZARD, 'Blizzard'),
        (GOG, 'GoG'),
        (HUMBLE_BUNDLE, 'Humble Bundle'),
        (ORIGIN, 'Origin'),
        (PSN, 'PSN'),
        (STEAM, 'Steam'),
        (OTHER, 'Other'),
    )


class Tag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tag'


class Game(models.Model):
    NOT_SYNCHED = 'NOT_SYNCHED'
    SYNCHED = 'SYNCHED'

    STATUS = (
        (NOT_SYNCHED, 'Not Synchronized'),
        (SYNCHED, 'Synchronized'),
    )

    RELEASE_MONTH = (
        (1, 'Jan'),
        (2, 'Feb'),
        (3, 'Mar'),
        (4, 'Apr'),
        (5, 'May'),
        (6, 'Jun'),
        (7, 'Jul'),
        (8, 'Aug'),
        (9, 'Sep'),
        (10, 'Oct'),
        (11, 'Nov'),
        (12, 'Dec'),
    )
    name = models.CharField(max_length=200)
    platforms = models.ManyToManyField(Platform, db_table='game_platform')
    genres = models.ManyToManyField(Genre, db_table='game_genre')
    release_year = models.PositiveSmallIntegerField(null=True)
    release_month = models.PositiveSmallIntegerField(null=True, choices=RELEASE_MONTH)
    release_day = models.PositiveSmallIntegerField(null=True)
    developer = models.OneToOneField(Developer, on_delete=models.PROTECT)
    publisher = models.OneToOneField(Publisher, on_delete=models.PROTECT)
    overview = models.TextField(null=True)
    esrb_rating = models.CharField(null=True, max_length=16, choices=ErsbRating.CATEGORIES)
    players = models.CharField(null=True, max_length=100)
    coop = models.NullBooleanField()
    rating = models.FloatField(null=True)
    location = models.CharField(null=True, max_length=100)
    notes = models.CharField(null=True, max_length=100)
    tags = models.ManyToManyField(Tag, db_table='game_tag')
    finished = models.NullBooleanField()
    original = models.NullBooleanField()
    playtime = models.PositiveIntegerField(null=True)
    youtube_url = models.URLField(null=True)
    logo_url = models.URLField(null=True)
    status = models.CharField(null=True, max_length=16, editable=False, choices=STATUS)
    store = models.CharField(null=True, max_length=32, choices=Store.SUPPORTED)
    store_game_id = models.CharField(null=True, max_length=36)
    created = models.DateTimeField(auto_now_add=True)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, db_table='user_game')

    def _platforms(self):
        return ", ".join((str(p) for p in self.platforms.all()))

    def _genres(self):
        return ", ".join((str(g) for g in self.genres.all()))

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'game'
