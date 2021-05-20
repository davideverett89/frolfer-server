from rest_framework import serializers
from frolferapi.models import Hole

class HoleSerializer(serializers.ModelSerializer):
    """JSON serializer for disc golf course holes.

    Arguments:
        serializers
    """
    class Meta:
        model = Hole
        fields = (
            'id',
            'label',
            'course_id'
        )