from rest_framework import serializers
from .player import PlayerSerializer
from frolferapi.models import Round

class RoundSerializer(serializers.ModelSerializer):
    """
    JSON serializer for player rounds.

    Arguments:
        serializers
    """

    player = PlayerSerializer(read_only=True)
    class Meta:
        model = Round
        fields = (
            'id',
            'score_card_id',
            'player_id',
            'total_strokes',
            'score',
            'player'
        )