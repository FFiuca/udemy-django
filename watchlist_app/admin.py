from django.contrib import admin

from watchlist_app.models import Movie, WatchList, StreamPlatform

# Register your models here.

admin.site.register(Movie)
admin.site.register(WatchList)
admin.site.register(StreamPlatform)
