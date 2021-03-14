"""File that contains the ScoreCard model"""

from django.db import models
from .player import Player
from .course import Course

class ScoreCard(models.Model):
    """
    Disc golf score card database model.
    """
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    player = models.ForeignKey(Player, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
