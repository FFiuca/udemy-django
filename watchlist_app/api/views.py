from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import (
    mixins,
    generics, # basically generics provide common CRUD function and we dont need write repeatly, just config the class
    viewsets
)
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly
from rest_framework.throttling import UserRateThrottle, AnonRateThrottle

from watchlist_app.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly, OnlyOneTimeInputReview
from watchlist_app.api.serializers import MovieSerializer, StreamPlatformSerializer, WatchListSerializer, StreamPlatformSerializer2, ReviewSerializer, ReviewSerializer2
from watchlist_app.models import Movie, WatchList, StreamPlatform, Review
from django.contrib.auth.models import User
from watchlist_app.api.paginations import DefaultPagination

# filter, order, pagination
class ReviewUser(generics.ListAPIView):
    queryset = Review.objects.all()
    serializer_class=ReviewSerializer2
    pagination_class = DefaultPagination

    def get_queryset(self):
        q = super().get_queryset()
        username = self.request.GET['username'] if 'username' in self.request.GET else None # ternary
        # print(username)
        # q = q.filter(user__username=username, watchlist__pk=1) # if you get parent table by child table, use field name for relationship
        q = q.filter(user__username=username).order_by('-created', 'rating')
        return q

class ReviewStandard(viewsets.ModelViewSet):
    queryset = Review.objects.all()
    serializer_class= ReviewSerializer2
    permission_classes=[IsAuthenticated]
    throttle_classes=[UserRateThrottle]

    # to return custom response
    def list(self, request, *args, **kwargs):
        data = self.get_serializer(self.get_queryset(), many=True).data
        data = {
            'status': 200,
            'data' : data
        }

        return Response(data=data, status=200)

# must test with postman also
# custom permission by base permission
class ReviewUpdatePerformHasUserUsePermission(viewsets.ModelViewSet):
    queryset = Review.objects.prefetch_related('watchlist', 'user').all()
    serializer_class = ReviewSerializer2
    permission_classes=[ReviewUserOrReadOnly] # https://www.django-rest-framework.org/api-guide/permissions/#api-reference
    throttle_classes = [UserRateThrottle, AnonRateThrottle] # it will auto determine throtle scope based on auth,

    # def get_queryset(self, ):
    #     query = super().get_queryset()

    #     if self.request.user.is_authenticated :
    #         query = query.filter(user=self.request.user)

    #     return query

    # still need check param url is not direct to review
    # user can't double input scenario
    def perform_update(self, serializer):
        # user = User.objects.get(pk=2)
        print('hhihi', self.request, self.kwargs,)
        # review = Review.objects.get(pk=self.kwargs['pk']) # doesn't need due use baseClassSerializer that already inject instance of selected review if use standard

        return serializer.save(data=self.request.data)


    def perform_create(self, serializer):
        user = self.request.user
        # watchlist = WatchList.objects.get(pk=self.request.data.get('watchlist'))
        watchlist = WatchList.objects.get(pk=1)

        count = watchlist.reviews.count() # reviews is related_name

        watchlist.sum_rating = count+ 1
        watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / watchlist.sum_rating

        watchlist.save()

        print('aaa',user, count, 'zzz', watchlist.sum_rating, watchlist.avg_rating, watchlist)
        # on djanga, every field relationship must select from master first
        return serializer.save(user=user, watchlist=watchlist)

# custom permission using old routing
class StreamPlatformCustomPermission(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer
    permission_classes=[AdminOrReadOnly]

# custom model view set
class StreamPlatformModelViewSet2(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.prefetch_related('watchlist').all() # to increase performance
    serializer_class = StreamPlatformSerializer

    # def get_queryset(self):
    #     return super().get_queryset().prefetch_related('watchlist') # to increase performance but when override with list function maybe, not carried away to queryset, must init manually

    # if use this doesn't need queryset instance anymore
    # def get_queryset(self):
    #     return StreamPlatform.objects.all()

    # can override too
    def list(self, request):
        # print(super().get_queryset().prefetch_related('watchlist'))
        queryset = super().get_queryset().exclude(pk=0).all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)


# ModelViewSets -> automate the model -> resource feature inlcudes
class StreamPlatformModelViewSet(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# custom ViewSets
class StreamPlatformViewSets2(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin ,
    viewsets.ViewSet
):
    # queryset = StreamPlatform.objects.all()


    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    # custom function name
    def list2(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def create2(self, request, *args, **kwargs):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)

        return Response(serializer.data)



# ViewSet and Routes -> like resource in laravel
# ViewSet will generate url based on function view class provided, ex: when you add create function, ViewSet will generate url that have post type, just little bit different than laravel
class StreamPlatformViewSets(viewsets.ViewSet):

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)

        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)


#override perform extends of mixins class
class ReviewCreatePerform(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer2

    def perform_create(self, serializer):
        print(self.kwargs, self.args, self.kwargs.get('pk_watchlist'))
        pk = self.kwargs['pk_watchlist']
        user = User.objects.get(pk=2)
        watchlist = WatchList.objects.get(pk=pk)

        return serializer.save(watchlist=watchlist, user=user)
        # return super().perform_create(serializer)

class ReviewCreatePerformHasUser(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer2
    permission_classes=[IsAuthenticatedOrReadOnly] # https://www.django-rest-framework.org/api-guide/permissions/#api-reference

    # user can't double input scenario
    def perform_create(self, serializer):
        # make user as default first due no login page
        # user = User.objects.get(pk=2)
        user = self.request.user
        watchlist = WatchList.objects.get(pk=self.kwargs['pk_watchlist'])

        checkEverReview = Review.objects.filter(watchlist=watchlist, user=user).exists()

        if(checkEverReview):
            raise ValidationError('The use has created review before.')


        return serializer.save(user=user, watchlist=watchlist)
        # return super().perform_create(self, serializer)

#override querysite extends of generics class
class ReviewListQueryset(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer2

    # logic : due generics.ListCreateAPIView class extends of genereic.APIView, so it will override get_queryset on genereic.APIView
    # both of them is can, at bottom one doesn't need queryset instance becase he return queryset itself
    def get_queryset(self):
        print(
            self.kwargs, # return dict
            self.args # return null tuple, it mean every url params will be provide by self.kwargs
        )

        pk = self.kwargs['pk_watchlist'] # it get from url params
        # pk = self.kwargs.get('pk')
        return super().get_queryset().filter(watchlist=pk)

    # def get_queryset(self):
    #     return Review.objects.filter(watchlist=self.kwargs['pk_watchlist'])

# generic concrete view class / shortcut of mixin and genericApiView
class ReviewListConcrete(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

class ReviewDetailConcrete(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # can custom also
    # def get(self, request, pk,*args, **kwargs):
    #     queryset = self.get_queryset().filter(pk=pk).all()
    #     serializer = self.serializer_class(queryset, many=True)
    #     return Response(serializer.data)

class ReviewDetail(mixins.RetrieveModelMixin, mixins.DestroyModelMixin, mixins.UpdateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # can be custom like this
    def get(self, request, pk,*args, **kwargs):
        queryset = self.get_queryset().filter(pk=pk).get()
        serializer = self.serializer_class(queryset)
        return Response(serializer.data)
        # return self.retrieve(request=request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request=request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request=request, *args, **kwargs)

class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request=request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        # print('haha',self.request.user)
        return self.create(request=request, *args, **kwargs)

class WatchListAV(APIView):

    def get(self, request) :
        movies = WatchList.objects.all()
        serializer = WatchListSerializer(movies, many=True)

        return Response(serializer.data)

    @api_view(('GET',))
    def other(request) :
        return Response({
            'status': 200
        })

class WatchListDetailAV(APIView):

    def get(self, request, pk):
        # print(self, pk)
        data = WatchList.objects.get(pk=pk)
        # print(data)
        serializer = WatchListSerializer(data, many=False).data

        return Response(serializer)

    def put(self, request, pk):
        movie = WatchList.objects.get(pk=pk)
        print(request.data, request)
        serializer = WatchListSerializer(movie, data=request.data)

        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)

class StreamPlatformAV(APIView):
    permission_classes=[IsAuthenticatedOrReadOnly]

    def get(self, request) :
        platform = StreamPlatform.objects.prefetch_related('watchlist').all()
        serializer = StreamPlatformSerializer(platform, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

class StreamPlatformAV2(APIView):

    def get(self, request) :
        platform = StreamPlatform.objects.prefetch_related('watchlist').all()
        serializer = StreamPlatformSerializer2(platform, many=True, context={'request': request})

        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

# same as resource in laravel
class StreamPlatformDetailAV(APIView):

    def get(self, request, pk) :
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform)

        return Response(serializer.data)

    def put(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        serializer = StreamPlatformSerializer(platform, data=request.data) # if update, old data must injected or it will create new one

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)

    def delete(self, request, pk):
        platform = StreamPlatform.objects.get(pk=pk)
        platform.delete()

        return Response(status=204)

@api_view(['GET'])
def getReview(request):
    # return Response({
    #     'data' : list(Review.objects.prefetch_related('watchlist').all().values())
    # }, status=200)

    data = Review.objects.prefetch_related('watchlist').all()
    ser = ReviewSerializer(data, many=True)

    return Response(ser.data)
