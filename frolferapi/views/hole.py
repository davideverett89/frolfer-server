"""View module for handling requests about disc golf course holes"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frolferapi.models import Hole

class Holes(ViewSet):
    """Frolfer disc golf course holes"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single disc golf course hole.

        Returns:
            Response -- JSON serialized disc golf course hole.
        """

        try:
            hole = Hole.objects.get(pk=pk)
            serializer = HoleSerializer(hole, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all disc golf course holes.

        Returns:
            Response -- JSON serialized list of all disc golf course holes.
        """

        holes = Hole.objects.all()
        serializer = HoleSerializer(
            holes, many=True, context={ 'request': request }
        )
        return Response(serializer.data)

class HoleSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf course holes.

    Arguments:
        serializers
    """
    class Meta:
        model = Hole
        fields = (
            'id',
            'label',
            'course_id'
        )
