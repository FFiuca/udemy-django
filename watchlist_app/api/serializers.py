from rest_framework import serializers, viewsets
from watchlist_app.models import Movie, StreamPlatform, WatchList, Review
from django.contrib.auth.admin import User
from virtualenv.app_data import read_only


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model= User
        exclude=['password']
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


class ReviewSerializer(serializers.ModelSerializer):
    watchlist_data = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(read_only=True)
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['watchlist']

    def get_watchlist_data(self, obj):
        # print('aa', type(obj.watchlist))
        return {
            'id' : obj.watchlist.id,
            'title' : obj.watchlist.title,
             'storyline' : obj.watchlist.storyline,
             'status_active' : obj.watchlist.status_active,
             'created' : obj.watchlist.created,
             'platform_id' : obj.watchlist.platform_id,
             'platform_data' : {
                'id' : obj.watchlist.platform.id,
                'name' : obj.watchlist.platform.name,
                'website' : obj.watchlist.platform.website,
             }
        }

class ReviewSerializer2(serializers.ModelSerializer):
    watchlist = serializers.PrimaryKeyRelatedField(read_only=False, queryset=WatchList.objects.all())
    # watchlist_data = serializers.SerializerMethodField(read_only=True)
    user = UserSerializer(read_only=True)
    # user = serializers.PrimaryKeyRelatedField(read_only=False) // error: must oveerid get_queryset
    class Meta:
        model = Review
        fields = '__all__'
        # exclude = ['watchlist']

    def get_watchlist_data(self, obj):
        # print('aa', type(obj.watchlist))
        return {
            'id' : obj.watchlist.id,
            'title' : obj.watchlist.title,
             'storyline' : obj.watchlist.storyline,
             'status_active' : obj.watchlist.status_active,
             'created' : obj.watchlist.created,
             'platform_id' : obj.watchlist.platform_id,
             'platform_data' : {
                'id' : obj.watchlist.platform.id,
                'name' : obj.watchlist.platform.name,
                'website' : obj.watchlist.platform.website,
             }
        }

class WatchListSerializer(serializers.ModelSerializer):
    reviews = ReviewSerializer(many=True, read_only=True)
    class Meta:
        model= WatchList
        exclude = []


class StreamPlatformSerializer(serializers.ModelSerializer):
    # column name must same with related_name in child table
    # read_only=True to prevent child table updated when program is performing the action. if you set False must override update function by your self
    watchlist = WatchListSerializer(many=True, read_only=True)

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
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # return __str__ value
    # watchlist = serializers.StringRelatedField(many=True)

    class Meta:
        model = StreamPlatform
        fields = '__all__'
        depth = 2

class StreamPlatformSerializer2(serializers.HyperlinkedModelSerializer):
    # column name must same with related_name in child table
    # read_only=True to prevent child table updated when program is performing the action. if you set False must override update function by your self
    watchlist = WatchListSerializer(many=True, read_only=True)

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
    # watchlist = serializers.PrimaryKeyRelatedField(many=True, read_only=True)

    # return __str__ value
    # watchlist = serializers.StringRelatedField(many=True)


    class Meta:
        model = StreamPlatform
        fields = '__all__'
        depth = 2
        extra_kwargs = {
            'url' : {
                'view_name' : 'watchlist_app:stream-detail',
                'lookup_field' : 'pk' # must unique column and pk is used for id column
            },
            # 'watchlist': {'lookup_field': 'pk'}
        }
