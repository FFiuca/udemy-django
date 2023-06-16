from django.urls import path

from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV

app_name = 'watchlist_app'
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('detail/<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/list', StreamPlatformAV.as_view(), name='stream.list'),
    path('stream/detail/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),


    path('other/', WatchListAV.other, name='other'),
]
