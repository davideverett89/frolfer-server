"""View module for handling requests about disc golf scorecards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework import serializers
from frolferapi.models import ScoreCard

class ScoreCards(ViewSet):
    """Frolfer disc golf scorecards"""

    def retrieve(self, request, pk=None):
        """Handle GET requests for a single scorecard.

        Returns:
            Response -- JSON serialized scorecards.
        """

        try:
            score_card = ScoreCard.objects.get(pk=pk)
            serializer = ScoreCardSerializer(score_card, context={ 'request': request })
            return Response(serializer.data)
        except Exception as ex:
            return HttpResponseServerError(ex)

    def list(self, request):
        """Handle GET requests to get all score cards.

        Returns:
            Response -- JSON serialized list of all score cards.
        """

        score_cards = ScoreCard.objects.all()
        serializer = ScoreCardSerializer(
            score_cards, many=True, context={ 'request': request }
        )
        return Response(serializer.data)

class ScoreCardSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf score cards.

    Arguments:
        serializers
    """

    class Meta:
        model = ScoreCard
        fields = (
            'id',
            'start_time',
            'end_time',
            'player',
            'course'
        )
