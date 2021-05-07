"""View module for handling requests about player rounds."""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frolferapi.models import Round

class Rounds(ViewSet):
    """Rounds played by Players per Scorecard"""

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


class RoundSerializer(serializers.ModelSerializer):
    """
    JSON serializer for player rounds.

    Arguments:
        serializers
    """

    class Meta:
        model = Round
        fields = (
            'id',
            'score_card_id',
            'player_id',
            'total_strokes',
            'score'
        )