from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import (
    mixins, 
    generics, # basically generics provide common CRUD function and we dont need write repeatly, just config the class
    viewsets
)

from watchlist_app.api.serializers import MovieSerializer, StreamPlatformSerializer, WatchListSerializer, StreamPlatformSerializer2, ReviewSerializer, ReviewSerializer2
from watchlist_app.models import Movie, WatchList, StreamPlatform, Review

# custom ViewSets
class StreamPlatformViewSets2(mixins.ListModelMixin, mixins.RetrieveModelMixin , viewsets.ViewSet):
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

    def retrieve(self, request, pk=None):
        queryset = StreamPlatform.objects.all()
        platform = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(platform)

        return Response(serializer.data)

# ViewSet and Routes -> like resource in laravel
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
        

#override perform extends of mixins class
class ReviewCreatePerform(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer2

    def perform_create(self, serializer):
        print(self.kwargs, self.args, self.kwargs.get('pk_watchlist'))
        pk = self.kwargs['pk_watchlist']
        watchlist = WatchList.objects.get(pk=pk)

        return serializer.save(watchlist=watchlist)
        # return super().perform_create(serializer)

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