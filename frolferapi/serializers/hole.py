from rest_framework import serializers
from .pin import PinSerializer
from frolferapi.models import Hole

class HoleSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf course holes.

    Arguments:
        serializers
    """

    pins = PinSerializer(many=True, read_only=True)
    class Meta:
        model = Hole
        fields = (
            'id',
            'label',
            'course_id',
            'pins'
        )