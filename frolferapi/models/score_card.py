"""File that contains the ScoreCard model"""

from django.db import models
from .course import Course

class ScoreCard(models.Model):
    """
    Disc golf score card database model.
    """
    start_time = models.DateTimeField(auto_now=True)
    end_time = models.DateTimeField(auto_now=True)
    course = models.ForeignKey(Course, on_delete=models.DO_NOTHING)
    condition = models.CharField(max_length=50, default="")
