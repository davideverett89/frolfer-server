"""View module for handling requests about player rounds."""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from frolferapi.models import Round
from frolferapi.serializers import RoundSerializer

class Rounds(ViewSet):
    """Rounds played by Players per Round"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single round played by someone.

        Returns:
            Response -- JSON serialized player round.
        """

        try:
            single_round = Round.objects.get(pk=pk)
            serializer = RoundSerializer(single_round, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all player rounds.

        Returns:
            Response -- JSON serialized list of all player rounds.
        """

        rounds = Round.objects.all()
        serializer = RoundSerializer(
            rounds, many=True, context={ 'request': request }
        )
        return Response(serializer.data)

    def create(self, request):
        '''Handle POST operations
        Returns:
            Response -- JSON serialized Round instance
        '''

        new_round = Round()

        new_round.score_card_id = request.data['score_card_id']
        new_round.player_id = request.data['player_id']
        new_round.total_strokes = request.data['total_strokes']
        new_round.score = request.data['score']

        new_round.save()

        serializer = RoundSerializer(new_round, context={'request': request})

        return Response(serializer.data)
