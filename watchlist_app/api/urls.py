from django.urls import path

from watchlist_app.api.views import WatchListAV, WatchListDetailAV, StreamPlatformAV, StreamPlatformDetailAV, StreamPlatformAV2, getReview, ReviewList, ReviewDetail, ReviewListConcrete, ReviewDetailConcrete

app_name = 'watchlist_app'
urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('detail/<int:pk>', WatchListDetailAV.as_view(), name='movie-detail'),
    path('stream/list', StreamPlatformAV.as_view(), name='stream.list'),
    path('stream/list2', StreamPlatformAV2.as_view(), name='stream.list2'),
    path('stream/detail/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-detail'),

    path('review/', ReviewList.as_view(), name='review'),
    path('review/<int:pk>', ReviewDetail.as_view(), name='review.detail'),

    # concrete
    path('review/concrete/', ReviewListConcrete.as_view(), name='review.concrete'),
    path('review/concrete/<int:pk>', ReviewDetailConcrete.as_view(), name='review.concrete.detail'),



    path('other/', WatchListAV.other, name='other'),
    path('getReview/', getReview, name='other.getReview'),
]
