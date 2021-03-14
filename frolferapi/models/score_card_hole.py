"""File that contains the ScoreCardHole model"""

from django.db import models
from .hole import Hole
from .score_card import ScoreCard

class ScoreCardHole(models.Model):
    """
    Disc golf score card hole database model.
    """
    score = models.IntegerField()
    hole = models.ForeignKey(Hole, models.DO_NOTHING)
    score_card = models.ForeignKey(ScoreCard, models.CASCADE)
