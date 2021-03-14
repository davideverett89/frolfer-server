"""File that contains the Player model"""

from django.db import models
from django.contrib.auth.models import User

class Player(models.Model):
    """
    Disc golf Player database model.
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
