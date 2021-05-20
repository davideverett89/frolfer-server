from rest_framework import serializers
from frolferapi.models import Round

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