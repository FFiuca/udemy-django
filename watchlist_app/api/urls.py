from django.urls import path, include
from rest_framework.routers import DefaultRouter

from watchlist_app.api.views import (
    WatchListAV,
    WatchListDetailAV,
    StreamPlatformAV,
    StreamPlatformDetailAV,
    StreamPlatformAV2,
    getReview,
    ReviewList,
    ReviewDetail,
    ReviewListConcrete,
    ReviewDetailConcrete,
    ReviewListQueryset,
    ReviewCreatePerform,
    StreamPlatformViewSets,
    StreamPlatformViewSets2,
    StreamPlatformModelViewSet,
    StreamPlatformModelViewSet2,
    ReviewCreatePerformHasUser,
    StreamPlatformCustomPermission,
    ReviewUpdatePerformHasUserUsePermission,
    ReviewStandard,
    ReviewUser,
    )

# only viewsets base class can be implement with router
router = DefaultRouter()
router.register('stream2', StreamPlatformViewSets, basename='streamplatform2')
router.register('stream3', StreamPlatformViewSets2, basename='streamplatform3')
router.register('stream5', StreamPlatformModelViewSet, basename='streamplatform5')
router.register('stream6', StreamPlatformModelViewSet2, basename='streamplatform5')
router.register('stream/custom-permissions', StreamPlatformCustomPermission, basename='stream.customPermission')
router.register('stream/validate-owner-data', ReviewUpdatePerformHasUserUsePermission, basename='review.validateOwnerData')
router.register('stream/standard', ReviewStandard, basename='review.standard')

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

    # override querysite based on pk_movie
    path(
        'stream/<int:pk_watchlist>/review',
        ReviewListQueryset.as_view(),
        # name='review.movie.filter'
    ),
    path(
        'stream/<int:pk_watchlist>/review-create',
        ReviewCreatePerform.as_view(),
        name='review.movie.create'
    ),
    path(
        'stream/<int:pk_watchlist>/review-create-has-user',
        ReviewCreatePerformHasUser.as_view(),
        name='review.movie.createHasUser'
    ),
    path(
        'stream/review/filter/',
        ReviewUser.as_view(),
        name='review.filter'
    ),


    # ViewSets
    path('', include(router.urls)),
    path('stream4', StreamPlatformViewSets2.as_view({
        'get' : 'list2', # custom view function, .as_view() only can use instead urlpatterns value
        'post' : 'create2',
    }), name='streamplatform4'),

    path('other/', WatchListAV.other, name='other'),
    path('getReview/', getReview, name='other.getReview'),
]
