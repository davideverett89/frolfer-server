"""File that contains the Tee model"""

from django.db import models
from .hole import Hole

class Pin(models.Model):
    """
    Disc golf pin database model.
    """
    label = models.CharField(max_length=50)
    par = models.IntegerField()
    length = models.CharField(max_length=50)
    hole = models.ForeignKey(Hole, on_delete=models.CASCADE)
    active = models.BooleanField(default=False)
