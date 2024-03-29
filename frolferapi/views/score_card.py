"""View module for handling requests about disc golf scorecards"""
from django.http import HttpResponseServerError
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from frolferapi.models import ScoreCard
from frolferapi.serializers import ScoreCardSerializer

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

    def create(self, request):
        '''Handle POST operations
        Returns:
            Response -- JSON serialized Scorecard instance
        '''

        new_scorecard = ScoreCard()

        new_scorecard.course_id = request.data['course_id']
        new_scorecard.condition = request.data['condition']

        new_scorecard.save()

        serializer = ScoreCardSerializer(new_scorecard, context={'request': request})

        return Response(serializer.data)
