from django.db import models

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

