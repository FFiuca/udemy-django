from django.db import models

# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    status_active = models.BooleanField(default=True)


    def __str__(self) -> str:
        return "id:{} name:{}".format(self. id, self.movie_name)
