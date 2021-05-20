from rest_framework import serializers
from frolferapi.models import RoundHole

class RoundHoleSerializer(serializers.ModelSerializer):
    """
    JSON serializer for round holes.

    Arguments:
        serializers
    """

    class Meta:
        model = RoundHole
        fields = (
            'id',
            'round_id',
            'hole_id',
            'strokes',
        )