from django.db import models

# Create your models here.
class MovieNames(models.Model):
    movieName = models.CharField(max_length = 50)
    
    def __str__(self):
        return self.movieName