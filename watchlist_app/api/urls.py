from django.urls import path

from watchlist_app.api.views import WatchListAV, WatchListDetailAV

app_name = 'watchlist_app'
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),

    path('detail/<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),

    path('other/', WatchListAV.other, name='other'),
]
