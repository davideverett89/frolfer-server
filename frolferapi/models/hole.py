"""File that contains the Hole model"""

from django.db import models
from .course import Course

class Hole(models.Model):
    """
    Disc golf Hole database model.
    """
    label = models.CharField(max_length=50)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
