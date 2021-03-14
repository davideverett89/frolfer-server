"""File that contains the Course model"""

from django.db import models

class Course(models.Model):
    """
    Disc golf Course database model.
    """
    name = models.CharField(max_length=50)
    holes = models.IntegerField()
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    zip_code = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    image_url = models.URLField(max_length=500)
