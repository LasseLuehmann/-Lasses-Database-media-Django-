from django.db import models

# Create your models here.
class Usage(models.Model):
    username = models.ForeignKey('user.User', on_delete=models.CASCADE)
    media_id = models.ForeignKey('media.Media', on_delete=models.CASCADE)
    start_date = models.DateField()
    end_date = models.DateField()
    