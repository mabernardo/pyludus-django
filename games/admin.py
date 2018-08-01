from django.contrib import admin

from .models import Game, Platform, Genre, Developer, Publisher, Tag


class GameAdmin(admin.ModelAdmin):
    list_display = ('name', '_platforms', '_genres', 'release_year', 'rating', 'store')
    list_filter = ('platforms', 'genres', 'developer', 'publisher', 'finished', 'original', 'status', 'store')


admin.site.register(Game, GameAdmin)
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Tag)
