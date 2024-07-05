from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.
class User(AbstractUser):
    username = models.CharField(max_length=30, primary_key=True)

    # class Meta:
    #     constraints = [
    #         models.CheckConstraint(
    #             name='%(app_label)s_%(class)s_username_validation_length_check',
    #             check=models.Q(username__gt=(len()>5))
    #         )
    #     ]