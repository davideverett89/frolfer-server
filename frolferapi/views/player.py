"""View module for handling requests about disc golf players"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from frolferapi.models import Player
from frolferapi.serializers import PlayerSerializer

class Players(ViewSet):
    """Frolfer disc golf players"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single disc player.

        Returns:
            Response -- JSON serialized disc golf player.
        """

        try:
            player = Player.objects.get(pk=pk)
            serializer = PlayerSerializer(player, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all disc golf players.

        Returns:
            Response -- JSON serialized list of all disc golf players.
        """

        players = Player.objects.all()
        serializer = PlayerSerializer(
            players, many=True, context={ 'request': request }
        )
        return Response(serializer.data)
