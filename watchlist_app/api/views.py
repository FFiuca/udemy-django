from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view, renderer_classes

from watchlist_app.api.serializers import MovieSerializer, StreamPlatformSerializer, WatchListSerializer
from watchlist_app.models import Movie, WatchList, StreamPlatform

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
        platform = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(platform, many=True)

        return Response(serializer.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid() :
            serializer.save()
            return Response(serializer.data)
        else :
            return Response(serializer.errors)
