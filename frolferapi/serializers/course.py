from rest_framework import serializers
from frolferapi.models import Course

class CourseSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf courses.

    Arguments:
        serializers
    """
    class Meta:
        model = Course
        fields = (
            'id',
            'name',
            'holes',
            'city',
            'state',
            'zip_code',
            'country',
            'image_url'
        )