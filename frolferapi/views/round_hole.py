"""View module for handling requests about round holes."""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from frolferapi.models import RoundHole
from frolferapi.serializers import RoundHoleSerializer

class RoundHoles(ViewSet):
    """A record of a player's performance on a single hole."""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single round hole.

        Returns:
            Response -- JSON serialized round holes.
        """

        try:
            single_round_hole = RoundHole.objects.get(pk=pk)
            serializer = RoundHoleSerializer(single_round_hole, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all round holes.

        Returns:
            Response -- JSON serialized list of all round holes.
        """

        round_holes = RoundHole.objects.all()
        serializer = RoundHoleSerializer(
            round_holes, many=True, context={ 'request': request }
        )
        return Response(serializer.data)
