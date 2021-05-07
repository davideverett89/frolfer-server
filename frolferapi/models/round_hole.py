"""File that contains the ScoreCardHole model"""

from django.db import models
from .hole import Hole
from .round import Round

class RoundHole(models.Model):
    """
    Disc golf round/hole database model.
    """
    round = models.ForeignKey(Round, models.CASCADE)
    hole = models.ForeignKey(Hole, models.DO_NOTHING)
    strokes = models.IntegerField()
