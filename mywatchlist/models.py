from django.db import models

class MyWatchList(models.Model):
    watched = models.CharField(max_length=50)
    title = models.CharField(max_length=70)
    rating = models.CharField(max_length=50)
    release_date = models.CharField(max_length=50)
    review = models.TextField()