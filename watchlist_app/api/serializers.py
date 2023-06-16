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
    # column name must same with related_name in child table
    # read_only=True to prevent child table updated when program is performing the action. if you set False must override update function by your self
    # watchlist = WatchListSerializer(many=True, read_only=True)

    # get single column of child
    # watchlist = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='title' # column name belonging child table want to show
    #  )

    # auto generate link
    # watchlist = serializers.HyperlinkedRelatedField(
    #     many=True,
    #     read_only=True,
    #     view_name='watchlist_app:movie-detail' # route name
    # )

    # return primary key
    watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # return __str__ value
    # watchlist = serializers.StringRelatedField(many=True)

    
    class Meta:
        model = StreamPlatform
        fields = '__all__'
        depth = 2