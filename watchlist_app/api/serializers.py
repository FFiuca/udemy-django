from rest_framework import serializers
from watchlist_app.models import Movie, StreamPlatform, WatchList

class MovieSerializer(serializers.ModelSerializer):
    #custom column, can use as casting or mutator on laravel
    len_movie_name = serializers.SerializerMethodField()

    class Meta:
        model= Movie
        exclude = []

    # def save(self, validatedData):
    #     data = {
    #                 **validatedData, 
    #                 'description': validatedData.description + ' cek'
    #             }
    #     return self.save(**data)

    def validate_movie_name(self, value):
        return value

    def get_len_movie_name(self, object):
        return len(object.movie_name)

class WatchListSerializer(serializers.ModelSerializer):
    class Meta:
        model= WatchList
        exclude = []


class StreamPlatformSerializer(serializers.ModelSerializer):
    class Meta:
        model = StreamPlatform
        fields = '__all__'