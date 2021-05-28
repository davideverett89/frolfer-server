from rest_framework import serializers
from frolferapi.models import ScoreCard

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
            'course',
            'condition'
        )
