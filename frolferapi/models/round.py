"""File that contains the Round model"""

from django.db import models
from .score_card import ScoreCard
from .player import Player

class Round(models.Model):
    """
    Player round database model.
    """
    score_card = models.ForeignKey(ScoreCard, on_delete=models.CASCADE)
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    total_strokes = models.IntegerField()
    score = models.IntegerField()
