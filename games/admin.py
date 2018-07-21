from django.contrib import admin

from .models import Game, Platform, Genre, Developer, Publisher, Tag

admin.site.register(Game)
admin.site.register(Platform)
admin.site.register(Genre)
admin.site.register(Developer)
admin.site.register(Publisher)
admin.site.register(Tag)
