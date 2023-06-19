from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes
from rest_framework import mixins, generics

from watchlist_app.api.serializers import MovieSerializer, StreamPlatformSerializer, WatchListSerializer, StreamPlatformSerializer2, ReviewSerializer
from watchlist_app.models import Movie, WatchList, StreamPlatform, Review


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