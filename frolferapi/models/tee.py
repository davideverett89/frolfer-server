"""File that contains the Tee model"""

from django.db import models
from .hole import Hole

class Tee(models.Model):
    """
    Disc golf tee database model.
    """
    par = models.IntegerField()
    length = models.CharField(max_length=50)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
