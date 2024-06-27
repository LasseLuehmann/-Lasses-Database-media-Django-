from django.db import models

# Create your models here.

class Platforms(models.Model):
    PL = {
        "PC": "Personal Computer",
        "PSP": "Play Station Portable",
        "PS": "Play Station",
        "PS2": "Play Station 2",
        "PS3": "Play Station 3",
        "PS4": "Play Station 4",
        "PS5": "Play Station 5",
        "Xbox": "Xbox",
        "Xbox360": "Xbox360",
        "XboxS": "Xbox Series S",
        "DVDp": "DVD player",
        "StSv": "Streaming Service"
    }
    platform = models.CharField(max_length=7, primary_key=True, choices=PL, default="PC")
    input_hardware = models.CharField(max_length=40)
    output_hardware = models.CharField(max_length=40)