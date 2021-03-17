"""View module for handling requests about disc golf courses"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frolferapi.models import Course

class Courses(ViewSet):
    """Frolfer disc golf courses"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single disc golf course.

        Returns:
            Response -- JSON serialized disc golf course.
        """

        try:
            course = Course.objects.get(pk=pk)
            serializer = CourseSerializer(course, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all disc golf courses.

        Returns:
            Response -- JSON serialized list of all disc golf courses.
        """

        courses = Course.objects.all()
        serializer = CourseSerializer(
            courses, many=True, context={ 'request': request }
        )
        return Response(serializer.data)

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
