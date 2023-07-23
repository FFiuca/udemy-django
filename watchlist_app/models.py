from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator, DecimalValidator
from django.contrib.auth.models import User

from watchlist_app.api.validators import preventDecimalNumber
# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    status_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return "id:{} name:{}".format(self. id, self.movie_name)


class StreamPlatform(models.Model):
    name = models.CharField(max_length=30)
    about = models.CharField(max_length=150)
    website = models.URLField()

    def __str__(self):
        return "id:{} name:{}".format(self.id, self.name)

class WatchList(models.Model):
    title = models.CharField(max_length=50)
    storyline = models.CharField(max_length=500)
    status_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    platform = models.ForeignKey(StreamPlatform, on_delete=models.CASCADE, related_name='watchlist', default=2)


    def __str__(self) -> str:
        return "id:{} name:{}".format(self. id, self.title)


class Review(models.Model):
    rating = models.PositiveIntegerField(
        default=None,
        null=True,
        validators=[
            MinValueValidator(0),
            MaxValueValidator(5),
            preventDecimalNumber,
        ]
    )

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    description = models.CharField(max_length=250, null=True)
    watchlist = models.ForeignKey(WatchList, on_delete=models.CASCADE, related_name='reviews')
    active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return 'id:{}, rating:{}, watchlist:{}'.format(self.id, self.rating, self.watchlist.title)
