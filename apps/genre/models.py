from django.db import models

# Create your models here.

class Genre(models.Model):
    genre_id = models.PositiveSmallIntegerField(primary_key=True)
    genre_name = models.CharField(max_length=20)
    describtion = models.TextField(null=True, blank=True)